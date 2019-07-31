# editor.py is part of Pylux
#
# Pylux is a program for the management of lighting documentation
# Copyright 2015 Jack Page
#
# Pylux is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pylux is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Edit the content of Pylux plot files.

editor is a CLI implementation of the Pylux plot editor, allowing 
for the reading and editing of Pylux plot files.
"""

import json
import math
import re
import uuid
from copy import deepcopy

import clihelper
from context.context import Context, Command
import document
from lib import data, printer, tagger


class EditorContext(Context):

    def __init__(self):
        """Registers commands."""
        super().__init__()
        self.name = 'editor'

        # Command Registration

        self.register(Command('ml', self.metadata_list, []))
        self.register(Command('mn', self.metadata_new, [
            ('ref', True, 'Reference to assign to the metadata.'),
            ('name', True, 'The name of the metadata to add.')]))
        self.register(Command('ms', self.metadata_set, [
            ('ref', True, 'The metadata to set the value of.'),
            ('value', True, 'Value for the metadata to take.')]))
        self.register(Command('mr', self.metadata_remove, [
            ('ref', True, 'The metadata to remove.')]))
        self.register(Command('mg', self.metadata_get, [
            ('name', True, 'Name of the metadata to print the value of.')]))
        self.register(Command('xn', self.fixture_new, [
            ('ref', True, 'The reference to give this new fixture.')]))
        self.register(Command('xN', self.fixture_from_template, [
            ('ref', True, 'The reference to give this new fixture.'),
            ('template', True, 'Path to the file to load data from.')]))
        self.register(Command('xc', self.fixture_clone, [
            ('src', True, 'The fixture to make a copy of.'),
            ('dest', True, 'References to clone the fixture to.')]))
        self.register(Command('xl', self.fixture_list, []))
        self.register(Command('xf', self.fixture_filter, [
            ('tag', True, 'The tag to filter by.'),
            ('value', True, 'The value the tag must be to be displayed.')]))
        self.register(Command('xr', self.fixture_remove, [
            ('ref', True, 'The fixture to remove.')]))
        self.register(Command('xg', self.fixture_get, [
            ('ref', True, 'The fixture to get a tag from.'),
            ('tag', True, 'The name of the tag to print the value of.')]))
        self.register(Command('xG', self.fixture_getall, [
            ('FIX', True, 'The fixture to print the tags of.')]))
        self.register(Command('xs', self.fixture_set, [
            ('FIX', True, 'The fixture to set a tag of.'),
            ('tag', True, 'The name of the tag to set.'),
            ('value', True, 'The value to set the tag to.')]))
        self.register(Command('xS', self.fixture_generate_autotags, [
            ('FIX', True, 'The fixture to generate tags for.'),
            ('target', False, 'The type of tags to generate. Omit for all.')]))
        self.register(Command('xa', self.fixture_address, [
            ('ref', True, 'The fixture to assign addresses to.'),
            ('reg', True, 'The name of the universe to address in.'),
            ('addr', True, 'The addresses to begin addressing at.')]))
        self.register(Command('xA', self.fixture_unaddress, [
            ('FIX', True, 'The fixture to unassign addresses for.')]))
        self.register(Command('xct', self.fixture_complete_from_template, [
            ('FIX', True, 'The fixture to update values of.'),
            ('template', True, 'Path to the file to load data from.')]))
        self.register(Command('rl', self.registry_list, []))
        self.register(Command('rq', self.registry_query, [
            ('REG', True, 'The registry to list used channels of.')]))
        self.register(Command('rn', self.registry_new, [
            ('ref', True, 'The reference to give this new registry.'),
            ('name', True, 'The name of the new registry.')]))
        self.register(Command('rr', self.registry_remove, [
            ('registry', True, 'The registry to remove.')]))
        self.register(Command('ra', self.registry_add, [
            ('FIX', True, 'The fixture the functions lie in to address.'),
            ('FNC', True, 'The range of functions within the fixture to patch.'),
            ('REG', True, 'Registry id to patch within.'),
            ('addr', True, 'The address to begin patching at.')]))
        self.register(Command('rS', self.registry_summarise, [
            ('REG', True, 'The registry to give an overview of.')]))
        self.register(Command('qn', self.cue_new_notrack, [
            ('ref', True, 'The reference to give this new cue.'),
            ('moves', False, 'The fixture movement data to initialise.')]))
        self.register(Command('qN', self.cue_new_track, [
            ('ref', True, 'The reference to give this new cue.'),
            ('moves', False, 'The moves to make relative from the previous cue.')]))
        self.register(Command('qr', self.cue_remove, [
            ('cue', True, 'The cue to remove.')]))
        self.register(Command('ql', self.cue_list, []))
        self.register(Command('qg', self.cue_get_intens, [
            ('cue', True, 'The cue to probe.')]))
        self.register(Command('qgx', self.cue_get_fixture_levels, [
            ('cue', True, 'The cue to probe.'),
            ('fix', True, 'The fixture(s) to match for.')]))
        self.register(Command('qs', self.cue_set, [
            ('cue', True, 'The cue to set the value of.'),
            ('tag', True, 'The key to assign this new value.'),
            ('value', True, 'The value to assign to this key.')]))
        self.register(Command('ia', self.import_ascii, [
            ('file', True, 'Patch of the ASCII file to import.'),
            ('target', True, 'The type of target to import from the file')]))

    def post_init(self):
        pass

    # Metadata commands

    def metadata_list(self, parsed_input):
        """List the values of all metadata in the plot file."""
        for meta in clihelper.refsort(document.get_metadata(self.plot_file)):
            clihelper.print_object(meta)

    def metadata_set(self, parsed_input):
        """Sets the value of a piece of metadata."""
        refs = clihelper.resolve_references(parsed_input[0])
        objs = [document.get_by_ref(self.plot_file, 'metadata', ref) for ref in refs]
        for obj in objs:
            obj['metadata-value'] = parsed_input[1]
            obj['name'] = parsed_input[1]

    def metadata_remove(self, parsed_input):
        '''Remove a piece of metadata from the file.'''
        refs = clihelper.resolve_references(parsed_input[0])
        for ref in refs:
            document.remove_by_ref(self.plot_file, 'metadata', ref)

    def metadata_get(self, parsed_input):
        '''Print the values of metadata matching a name.'''
        for match in document.get_by_value(self.plot_file, 'metadata-key', parsed_input[0]):
            clihelper.print_object(match)

    def metadata_new(self, parsed_input):
        '''Create a new metadata item.'''
        if parsed_input[0] == 'auto':
            refs = [document.autoref(self.plot_file, 'metadata')]
        else:
            refs = clihelper.resolve_references(parsed_input[0])
        for ref in refs:
            self.plot_file.append({
                'type': 'metadata',
                'uuid': str(uuid.uuid4()),
                'ref': ref,
                'name': parsed_input[1],
                'metadata-key': parsed_input[1]
            })

    # Fixture commands

    def fixture_new(self, parsed_input):
        '''Create a new fixture from scratch.'''
        if parsed_input[0] == 'auto':
            refs = [document.autoref(self.plot_file, 'fixture')]
        else:
            refs = clihelper.resolve_references(parsed_input[0])
        for ref in refs:
            self.plot_file.append({
                'type': 'fixture',
                'uuid': str(uuid.uuid4()),
                'ref': ref
            })

    def fixture_from_template(self, parsed_input):
        '''Create a new fixture from a template file.'''
        if parsed_input[0] == 'auto':
            refs = [document.autoref(self.plot_file, 'fixture')]
        else:
            refs = clihelper.resolve_references(parsed_input[0])
        template_file = data.get_data('fixture/'+parsed_input[1]+'.json')
        if not template_file:
            print('Template {0} does not exist, reverting to fallback.'.format(parsed_input[1]))
            template_file = data.get_data('fixture/'+self.config['editor']['fallback-template']+'.json')
        with open(template_file) as f:
            fixture = json.load(f)
        for ref in refs:
            fixture['ref'] = ref
            fixture['uuid'] = str(uuid.uuid4())
            if 'personality' in fixture:
                for function in fixture['personality']:
                    function['uuid'] = str(uuid.uuid4())
            self.plot_file.append(fixture)

    def fixture_clone(self, parsed_input):
        '''Create a new fixture by copying an existing fixture.'''
        src = document.get_by_ref(self.plot_file, 'fixture', int(parsed_input[0]))
        dest = clihelper.resolve_dec_references(parsed_input[1])
        for loc in dest:
            new = dict.copy(src)
            new['uuid'] = str(uuid.uuid4())
            new['ref'] = loc
            self.plot_file.append(new)

    def fixture_list(self, parsed_input):
        '''List all fixtures in the plot file.'''
        for fix in clihelper.refsort(document.get_by_type(self.plot_file, 'fixture')):
            clihelper.print_object(fix)

    def fixture_filter(self, parsed_input):
        '''List all fixtures that meet a certain criterion.'''
        k = parsed_input[0]
        v = parsed_input[1]
        fixtures = document.get_by_type(self.plot_file, 'fixture')
        for match in document.get_by_value(fixtures, k, v):
            clihelper.print_object(match)

    def fixture_remove(self, parsed_input):
        '''Remove a fixture from the plot file.'''
        refs = clihelper.safe_resolve_dec_references(self.plot_file, 'fixture', parsed_input[0])
        for ref in refs:
            document.remove_by_ref(self.plot_file, 'fixture', ref)

    def fixture_get(self, parsed_input):
        '''Print the values of all a fixture's tags.'''
        refs = clihelper.safe_resolve_dec_references(self.plot_file, 'fixture', parsed_input[0])
        for ref in refs:
            f = document.get_by_ref(self.plot_file, 'fixture', ref)
            clihelper.print_object(f)
            print(str(len(f)), 'Data Tags:')
            for k, v in sorted(f.items()):
                print('    '+str(k)+': '+str(v))

    def fixture_getall(self, parsed_input):
        '''Print the tags and functions of a fixture..'''
        refs = clihelper.safe_resolve_dec_references(self.plot_file, 'fixture', parsed_input[0])
        for ref in refs:
            f = document.get_by_ref(self.plot_file, 'fixture', ref)
            clihelper.print_object(f)
            print(str(len(f)), 'Data Tags:')
            for k, v in sorted(f.items()):
                print('    ' + str(k) + ': ' + str(v))
            if len(f['personality']):
                print(str(len(f['personality'])), 'DMX Functions:')
                for func in f['personality']:
                    print('   ', printer.get_generic_string(func))

    def fixture_set(self, parsed_input):
        '''Set the value of one of a fixture's tags.'''
        refs = clihelper.safe_resolve_dec_references(self.plot_file, 'fixture', parsed_input[0])
        objs = [document.get_by_ref(self.plot_file, 'fixture', ref) for ref in refs]
        for obj in objs:
            obj[parsed_input[1]] = parsed_input[2]

    def fixture_address(self, parsed_input):
        '''Assign DMX addresses to a fixture.'''
        refs = clihelper.resolve_references(parsed_input[0])
        univ = int(parsed_input[1])
        reg = document.get_by_ref(self.plot_file, 'registry', univ)
        while not reg:
            print('No registry with id {0}, creating a new one'.format(univ))
            self.registry_new([str(univ)])
            reg = document.get_by_ref(self.plot_file, 'registry', univ)
        for ref in refs:
            f = document.get_by_ref(self.plot_file, 'fixture', ref)
            n = len(f['personality'])
            if n > 0 and parsed_input[2] not in ['0', 0]:
                if parsed_input[2] == 'auto':
                    addr = document.get_start_address(reg, n)
                else:
                    addr = int(parsed_input[2])
                for func in f['personality']:
                    if addr > 512:
                        univ += 1
                        reg = document.get_by_ref(self.plot_file, 'registry', univ)
                        while not reg:
                            print('No registry with id {0}, creating a new one'.format(univ))
                            self.registry_new([str(univ)])
                            reg = document.get_by_ref(self.plot_file, 'registry', univ)
                        addr = addr % 512
                    reg['table'][addr] = func['uuid']
                    addr += 1

    def fixture_unaddress(self, parsed_input):
        """Remove all entries for functions in this fixture which appear in any registry."""
        refs = clihelper.resolve_references(parsed_input[0])
        for ref in refs:
            f = document.get_by_ref(self.plot_file, 'fixture', ref)
            funcs = [func['uuid'] for func in f['personality']]
            for reg in document.get_by_type(self.plot_file, 'registry'):
                for d in deepcopy(reg['table']):
                    if reg['table'][d] in funcs:
                        del reg['table'][d]

    def fixture_complete_from_template(self, parsed_input):
        """Compare a fixture with a specified template. If any tags exist in
        the template and not the fixture, add them from the template. Do not
        overwrite any existing tags in the fixture."""
        refs = clihelper.resolve_references(parsed_input[0])
        template_file = data.get_data('fixture/' + parsed_input[1] + '.json')
        if not template_file:
            print('Template does not exist')
        else:
            for ref in refs:
                dest = document.get_by_ref(self.plot_file, 'fixture', int(ref))
                with open(template_file) as f:
                    source = json.load(f)
                for tag in source:
                    if tag not in dest:
                        dest[tag] = source[tag]
                if 'personality' in source:
                    if 'personality' not in dest:
                        dest['personality'] = source['personality']
                        for func in dest['personality']:
                            func['uuid'] = str(uuid.uuid4())
                    else:
                        existing_funcs = [i['name'] for i in dest['personality']]
                        for func in source['personality']:
                            if func['name'] not in existing_funcs:
                                func['uuid'] = str(uuid.uuid4())
                                dest['personality'].append(func)

    def fixture_generate_autotags(self, parsed_input):
        """Uses the tagger class to automatically populate tags in fixtures."""
        refs = clihelper.resolve_references(parsed_input[0])
        if len(parsed_input) < 2:
            target = 'all'
        else:
            target = parsed_input[1]
        function_map = {'all': tagger.tag_fixture_all,
                        'colour': tagger.tag_fixture_colour,
                        'rotation': tagger.tag_fixture_rotation,
                        'patch': tagger.tag_fixture_patch}
        for ref in refs:
            f = document.get_by_ref(self.plot_file, 'fixture', int(ref))
            function_map[target](self.plot_file, f)

    # Registry commands

    def registry_new(self, parsed_input):
        '''Create a new registry.'''
        if parsed_input[0] == 'auto':
            refs = [document.autoref(self.plot_file, 'registry')]
        else:
            refs = clihelper.resolve_references(parsed_input[0])
        for ref in refs:
            self.plot_file.append({
                'type': 'registry',
                'uuid': str(uuid.uuid4()),
                'ref': ref,
                'table': {}
            })

    def registry_remove(self, parsed_input):
        '''Delete one or more registries.'''
        refs = clihelper.resolve_references(parsed_input[0])
        for ref in refs:
            document.remove_by_ref(self.plot_file, 'registry', ref)

    def registry_list(self, parsed_input):
        '''List all registries.'''
        for reg in clihelper.refsort(document.get_by_type(self.plot_file, 'registry')):
            clihelper.print_object(reg)

    def registry_query(self, parsed_input):
        '''List the functions of all used channels in a registry.'''
        refs = clihelper.resolve_references(parsed_input[0])
        for ref in refs:
            r = document.get_by_ref(self.plot_file, 'registry', ref)
            clihelper.print_object(r)
            t = {int(i): r['table'][i] for i in r['table']}
            print(str(len(t)), 'Used Addresses:')
            for k, v in sorted(t.items()):
                func = document.get_function_by_uuid(self.plot_file, v)
                f = document.get_function_parent(self.plot_file, func)
                print(''.join(['DMX',str(format(k, '03d')),': ',
                               printer.get_generic_string(f),' (',
                               printer.get_generic_string(func),')']))

    def registry_add(self, parsed_input):
        """Manually assign one function in a registry table."""
        fix = document.get_by_ref(self.plot_file, 'fixture', clihelper.resolve_references(parsed_input[0])[0])
        func_refs = clihelper.resolve_references(parsed_input[1])
        reg = document.get_by_ref(self.plot_file, 'registry', parsed_input[2])
        while not reg:
            print('No registry with id {0}, creating a new one'.format(parsed_input[2]))
            self.registry_new([str(parsed_input[2])])
            reg = document.get_by_ref(self.plot_file, 'registry', int(parsed_input[2]))
        addr = int(parsed_input[3])
        for func in func_refs:
            uuid = document.get_by_value(fix['personality'], 'offset', func)['uuid']
            reg['table'][addr] = uuid
            addr += 1

    def registry_summarise(self, parsed_input):
        """Show a table of DMX addresses of a registry to see at a glance which addresses are occupied."""
        refs = clihelper.resolve_references(parsed_input[0])
        for ref in refs:
            r = document.get_by_ref(self.plot_file, 'registry', ref)
            clihelper.print_object(r)
            current_row = '   '
            width = int(self.config['cli']['registry-summary-width'])
            for i in range(0, width):
                current_row += ' '+str(format(i, '02d'))
            for i in range(1, 514):
                if i % width == 1 or i == 513:
                    print(current_row)
                    current_row = str(format(i, '03d')) + '  '
                if str(i) in r['table'] or i in r['table']:
                    current_row += '\033[31m#\033[0m  '
                else:
                    current_row += '\033[92m-\033[0m  '

    # Cue commands

    def cue_new_notrack(self, parsed_input):
        """Create a new cue."""
        if parsed_input[0] == 'auto':
            refs = [document.autoref(self.plot_file, 'cue')]
        else:
            refs = clihelper.resolve_dec_references(parsed_input[0])

        levels = []
        if len(parsed_input) == 2:
            raw = parsed_input[1]
            for level in raw.split(';'):
                frefs = clihelper.resolve_dec_references(level.split('@')[0])
                for ref in frefs:
                    f = document.get_by_ref(self.plot_file, 'fixture', ref)
                    # Search through fixture functions for first function which 
                    # controls intensity, and assume that this is the master 
                    # intensity, then add this to the move instruction.
                    for function in f['personality']:
                        if function['parameter'] == 'Intensity':
                            func = function['uuid']
                            levels.append({'func': func, 'level': level.split('@')[1]})

        for ref in refs:
            self.plot_file.append({
                'type': 'cue',
                'uuid': str(uuid.uuid4()),
                'ref': ref,
                'levels': levels,
            })

    def cue_new_track(self, parsed_input):
        """Create a new cue, tracking forward values from the previous cue."""
        pass

    def cue_remove(self, parsed_input):
        '''Remove a cue.'''
        refs = clihelper.safe_resolve_dec_references(parsed_input[0])
        for ref in refs:
            document.remove_by_ref(self.plot_file, 'cue', ref)

    def cue_list(self, parsed_input):
        '''List all cues'''
        for cue in clihelper.refsort(document.get_by_type(self.plot_file, 'cue')):
            clihelper.print_object(cue)

    def cue_get_intens(self, parsed_input):
        """Display the fixture intensity levels in a cue."""
        refs = clihelper.safe_resolve_dec_references(self.plot_file, 'cue', parsed_input[0])
        for ref in refs:
            q = document.get_by_ref(self.plot_file, 'cue', ref)
            clihelper.print_object(q)
            for level in q['levels']:
                func = document.get_function_by_uuid(self.plot_file, level['func'])
                if func['param'] == 'Intens':
                    f = document.get_function_parent(self.plot_file, func)
                    bar = printer.ProgressBar()
                    bar += level['level']
                    print(''.join([
                        printer.get_generic_ref(f),
                        str(bar)]))

    def cue_get_fixture_levels(self, parsed_input):
        """Get the values of all parameters of a particular fixture in a given cue."""
        cue_refs = clihelper.safe_resolve_dec_references(self.plot_file, 'cue', parsed_input[0])
        for cue_ref in cue_refs:
            cue = document.get_by_ref(self.plot_file, 'cue', cue_ref)
            clihelper.print_object(cue)
            fix_refs = clihelper.safe_resolve_dec_references(self.plot_file, 'fixture', parsed_input[1])
            for fix_ref in fix_refs:
                fix = document.get_by_ref(self.plot_file, 'fixture', fix_ref)
                intens_uuid = document.find_fixture_intens(fix)['uuid']
                for level in cue['levels']:
                    func = document.get_function_by_uuid(self.plot_file, level['func'])
                    if func['uuid'] == intens_uuid:
                        bar = printer.ProgressBar()
                        bar += level['level']
                        print(''.join([printer.get_generic_ref(fix), str(bar)]))
                    if document.get_function_parent(self.plot_file, func) == fix:
                        print('    '+printer.get_generic_string(func)+' @ '+str(level['level']))

    def cue_set(self, parsed_input):
        """Set the value of a tag in a cue."""
        refs = clihelper.safe_resolve_dec_references(self.plot_file, 'cue', parsed_input[0])
        objs = [document.get_by_ref(self.plot_file, 'cue', ref) for ref in refs]
        for obj in objs:
            obj[parsed_input[1]] = parsed_input[2]

    def cue_set_fixture_level(self, parsed_input):
        """Set the level of a fixture's intensity for a cue."""
        cue_refs = clihelper.safe_resolve_dec_references(self.plot_file, 'cue', parsed_input[0])
        fix_refs = clihelper.safe_resolve_dec_references(self.plot_file, 'fixture', parsed_input[1])
        level = parsed_input[2]
        if level[0] == 'H':
            # Convert hexadecimal strings to integers
            level = int(level[1:3], 16)
        for cue_ref in cue_refs:
            cue = document.get_by_ref(self.plot_file, 'cue', cue_ref)
            for fix_ref in fix_refs:
                fix = document.get_by_ref(self.plot_file, 'fixture', fix_ref)
                intens_func = document.find_fixture_intens(fix)
                cue['levels'].append({'func': intens_func['uuid'], 'level': level})

    def _cue_set_function_level(self, cue, func, level):
        """Set the level of a function, in a cue."""
        fix = document.get_function_parent(self.plot_file, func)
        # Check to see if the function is a 16 bit function by checking for
        # functions with the (16b) suffix with the same name
        fine_func = document.get_by_value(fix['personality'], 'param', func['param']+' (16b)')
        if fine_func:
            # Logic to determine 16bit values
            upper_bit = math.floor(int(level)/256)
            lower_bit = int(level) % 256
            cue['levels'].append({'func': func['uuid'], 'level': upper_bit})
            cue['levels'].append({'func': fine_func[0]['uuid'], 'level': lower_bit})
        else:
            cue['levels'].append({'func': func['uuid'], 'level': level})

    # Import commands

    def import_ascii(self, parsed_input):
        """
        Import data from a USITT ASCII file, such as that exported by ETC Eos.
        Specify a data target to import.
        Supported targets are:
            conventional_patch: Reads Patch lines only. Only supports dimmer
            patching, which will be patched using the template defined in the
            config.
            eos_patch: Reads special $Patch lines added by Eos, which support
            database values and personalities.
        """
        target = parsed_input[1]
        with open(parsed_input[0]) as f:
            raw = f.readlines()

        def extract_blocks(start_regex):
            # Utility function to extract blocks of data beginning with given
            # regex pattern and ending with a blank line. Returns as a list
            # of lines for easy parsing.
            blocks = []
            current_block = []
            start_r = re.compile(start_regex)
            end_r = re.compile('^\s*$')
            for l in raw:
                if re.match(start_r, l):
                    current_block.append(l)
                if current_block != []:
                    # We only want to perform the following functions if we're
                    # already in a block, to prevent adding the whole document.
                    if re.match(end_r, l):
                        blocks.append(current_block)
                        current_block = []
                    else:
                        current_block.append(l)
            return blocks

        def resolve_line(line):
            # Strips down lines in blocks and returns them in a key/value
            # format.
            line = line.lstrip()
            line = line.strip()
            return line.split(' ', maxsplit=1)

        # Look through parameters saved in this ASCII file and make our
        # own list to we can refer to them later.
        parameters = {}
        r = re.compile('\$ParamType +([0-9]*) ([0-9]*) (.*)')
        for l in raw:
            match = re.match(r, l)
            if match:
                parameters[match.group(1)] = match.group(3).strip()

        if target == 'conventional_patch':
            entries = []
            r = re.compile('Patch.*')
            # Scan file for lines beginning with the Patch keyword and populate
            # into list for parsing.
            for l in raw:
                match = re.match(r, l)
                if match: entries.append(match.string)
            # For each patch line found, find each mapping within the line and
            # add to the plot file using the built in command.
            r = re.compile('[0-9]*<[0-9]{0,3}')
            template = self.config['ascii']['conventional-template']
            for e in entries:
                maps = re.findall(r, e)
                for f in maps:
                    ref = f.split('<')[0]
                    addr = int(f.split('<')[1])
                    dmx = addr%512
                    univ = math.floor(addr/512)
                    self.fixture_from_template([ref, template])
                    self.fixture_address([ref, univ, dmx])

        elif target == 'eos_patch':
            personality_blocks = extract_blocks('\$Personality.*')
            patch_blocks = extract_blocks('\$Patch.*')
            templates = {}

            # Look through personalities saved in this ASCII file and make our
            # own list of them so we can refer to them later.
            for block in personality_blocks:
                pers_ref = block[0].split(' ')[1]
                pers = []
                template = {'type': 'fixture'}
                for l in block:
                    res = resolve_line(l)
                    if res[0] == '$$Manuf':
                        template['manufacturer'] = res[1]
                    elif res[0] == '$$Model':
                        template['fixture-type'] = res[1]
                    elif res[0] == '$$PersChan':
                        pers.append({
                            'type': 'function',
                            'param': parameters[res[1].split()[0]],
                            'offset': int(res[1].split()[2]),
                        })
                        if int(res[1].split()[1]) == 2:
                            pers.append({
                                'type': 'function',
                                'param': parameters[res[1].split()[0]]+' (16b)',
                                'offset': int(res[1].split()[3])
                            })
                template['personality'] = pers
                templates[pers_ref.strip()] = template

            for patch in patch_blocks:
                fix_ref = patch[0].split(' ')[1]
                # We have to make a deep copy of the template, to ensure that
                # we aren't adjusting the personality and functions in place
                # when we add UUIDs
                template = deepcopy(templates[patch[0].split(' ')[2]])
                addr = int(patch[0].split(' ')[3])
                dmx = addr % 512
                univ = math.floor(addr / 512)
                self.fixture_new([fix_ref])
                for k in template:
                    self.fixture_set([fix_ref, k, template[k]])
                document.fill_missing_function_uuids(document.get_by_ref(self.plot_file, 'fixture', int(fix_ref)))
                # Patch the fixture from the address in the @Patch line
                self.fixture_address([fix_ref, univ, dmx])
                # We've dealt with the main @Patch line, now we can scan through
                # the rest of the block and see if we can merge in anything else.
                for l in patch:
                    res = resolve_line(l)
                    if res[0] == '$$TextGel':
                        self.fixture_set([fix_ref, 'gel', res[1]])
                    if res[0] == 'Text':
                        self.fixture_set([fix_ref, 'label', res[1]])

        elif target == 'cues':
            cue_blocks = extract_blocks('Cue.*')
            for cue in cue_blocks:
                cue_ref = cue[0].split()[1]
                self.cue_new_notrack([cue_ref])
                for l in cue:
                    res = resolve_line(l)
                    if res[0] == 'Text':
                        self.cue_set([cue_ref, 'label', res[1]])
                    elif res[0] == 'Up':
                        self.cue_set([cue_ref, 'fade-up', res[1]])
                    elif res[0] == 'Down':
                        self.cue_set([cue_ref, 'fade-down', res[1]])
                    elif res[0] == 'Chan':
                        for level in res[1].split():
                            self.cue_set_fixture_level([cue_ref,
                                                        level.split('@')[0],
                                                        level.split('@')[1]])
                    elif res[0] == '$$Param':
                        fixture = document.get_by_ref(self.plot_file, 'fixture', res[1].split()[0])
                        for param_level in res[1].split():
                            if '@' in param_level:
                                param_type = parameters[param_level.split('@')[0]]
                                # If this parameter is Intens, it will be referring to a 16 bit value, which we have
                                # probably already added as an 8 bit from the generic levels lines. Therefore, we will
                                # remove the 8 bit entry and replace with this 16 bit entry.
                                if param_type == 'Intens':
                                    intens_uuid = document.find_fixture_intens(fixture)['uuid']
                                    cue_levels = document.get_by_ref(self.plot_file, 'cue', cue_ref)['levels']
                                    for level in cue_levels:
                                        if level['func'] == intens_uuid:
                                            cue_levels.remove(level)
                                param_value = param_level.split('@')[1]
                                func = document.get_by_value(fixture['personality'], 'param', param_type)[0]
                                self._cue_set_function_level(document.get_by_ref(self.plot_file, 'cue', cue_ref),
                                                             func, param_value)

        else:
            print('Unsupported target. See the help page for this command for a list of supported targets.')


def get_context():
    return EditorContext()
