# reporter.py is part of Pylux
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

"""Generate text reports from Jinja templates.

Reporter uses a Jinja2 template to generate documentation from the 
plot file. It was made primarily for LaTeX documentation but could 
just as easily be used for other formats.
"""

from jinja2 import Environment, FileSystemLoader
import os
import pylux.plot as plot
import pylux.clihelper as clihelper
from pylux import get_data
from pylux.context.context import Context, Command


class Report:

    def __init__(self, plot_file):
        self.environment = Environment(lstrip_blocks=True, trim_blocks=True, 
                                loader=FileSystemLoader(get_data('template/')))
        self.plot_file = plot_file

    def find_template(self, template):
        all_templates = os.listdir(get_data('template'))
        discovered = {}
        for template_file in all_templates:
            if template_file.split('.')[0] == template:
                discovered[template_file.split('.')[1]] = template_file
        return discovered
        

    def generate(self, template, options):
        """Generate a report.

        Args
            template: full name, including extension of the template
            options: dict of options
        """
        template = self.environment.get_template(template)
        cue_list = sorted(plot.CueList(self.plot_file).cues,
                          key=lambda cue: cue.key)
        fixture_list = plot.FixtureList(self.plot_file).fixtures
        metadata_list = plot.Metadata(self.plot_file).meta
        self.content = template.render(cues=cue_list, fixtures=fixture_list,
                                       meta=metadata_list, options=options)


class ReporterContext(Context):

    def __init__(self):
        self.name = 'reporter'
        self.init_commands()
        self.register(Command('rn', self.report_new, ['template', 'options'], 
                      synopsis='Create a new report from the Jinja template ' 
                               'and pass in the options.'))
        self.register(Command('rg', self.report_get, [], 
                      synopsis='Print the report buffer.'))
        self.register(Command('rw', self.report_write, ['path'], 
                      synopsis='Write the report buffer to a file.'))

    def report_new(self, parsed_input):
        self.report = Report(self.plot_file)

        def get_options(parsed_input):
            if len(parsed_input) > 1:
                options = {}
                options_input = parsed_input[1].split(';')
                for option in options_input:
                    options[option.split('=')[0]] = option.split('=')[1]
                return options

        def get_template(self, parsed_input):
            possible_templates = self.report.find_template(parsed_input[0])
            if len(possible_templates) == 0:
                return None
            elif len(possible_templates) == 1:
                return list(possible_templates.values())[0]
            else:
                print('The template you entered has '+
                      str(len(possible_templates))+' matches: ')
                print(possible_templates)
                ext = input('Choose an extension to continue: ')
                return possible_templates[ext]
        
        options = get_options(parsed_input)
        template = get_template(self, parsed_input)
        if template != None:
            self.report.generate(template, options)
            
    def report_get(self, parsed_input):
        print(self.report.content)

    def report_write(self, parsed_input):
        with open(os.path.expanduser(parsed_input[0]), 'w') as outfile:
            outfile.write(self.report.content)


def get_context():
    return ReporterContext()
