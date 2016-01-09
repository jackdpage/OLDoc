# reference.py is part of Pylux
#
# Pylux is a program for the management of lighting documentation
# Copyright 2015 Jack Page
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

gel_colours = {
# Rosco stagedepot.co.uk HTML swatches
    '#24': '#f50014',
    '127': '#e16273',
    '166': '#f06165',
    '24': '#ff5a64',
    '157': '#ff92a3',
    '185': '#d5bfc1',
    '186': '#dcb9bd',
    '107': '#ffa5af',
    '248': '#ffe2e4',
    '787': '#b9003c',
    '#50': '#bb002c',
    '27': '#c8003c',
    '#26': '#d70229',
    '46': '#dc005a',
    '29': '#e1003c',
    '26': '#e6003c',
    '#46': '#eb016d',
    '106': '#f00032',
    '113': '#ff0064',
    '#324': '#f50f39',
    '#339': '#ff1283',
    '#342': '#ff1562',
    '#332': '#ff2957',
    '332': '#ff3787',
    '#343': '#ff397f',
    '#43': '#ff3e93',
    '148': '#ff507d',
    '748': '#e96785',
    '#36': '#ff6d96',
    '#336': '#ff73b7',
    '111': '#ff8cbe',
    '192': '#ff8cb4',
    '36': '#ffa0b9',
    '#35': '#ffa7bb',
    '#337': '#ffafc2',
    '110': '#ffb4c8',
    '247': '#fac3d7',
    '#33': '#ffc2d0',
    '35': '#ffc8d2',
    '249': '#ffecf0',
    '49': '#be0091',
    '126': '#be009b',
    '#39': '#e800bc',
    '#344': '#ff05d3',
    '#346': '#ff2dd5',
    '341': '#bc7da8',
    '793': '#ff3ca0',
    '795': '#fa46c8',
    '128': '#ff50b4',
    '48': '#e66eaf',
    '328': '#ff64c8',
    '2': '#ff78dc',
    '170': '#e6aadc',
    '136': '#f0bee6',
    '794': '#ffafdc',
    '#38': '#ffbbe2',
    '39': '#ffbde1',
    '169': '#fadcf0',
    '797': '#af0096',
    '798': '#a000be',
    '#49': '#c900e6',
    '#349': '#f000ff',
    '#47': '#cc4eb9',
    '345': '#cd6ed7',
    '703': '#d282dc',
    '704': '#f0aafa',
    '705': '#efaafa',
    '707': '#6400b4',
    '700': '#7d00cd',
    '343': '#8c00d2',
    '#347': '#b101dd',
    '#358': '#8e0aea',
    '#348': '#da2dff',
    '701': '#b45adc',
    '58': '#b46ef0',
    '194': '#be8cf0',
    '52': '#e6aafa',
    '702': '#e6d2f0',
    '#54': '#e6c7ff',
    '#351': '#efdcff',
    '750': '#f9f1fe',
    '#382': '#250070',
    '181': '#5000aa',
    '799': '#3c00b4',
    '#385': '#4f02cf',
    '#74': '#4200ff',
    '#374': '#4200ff',
    '#59': '#7200ff',
    '706': '#6e46c8',
    '#377': '#7124ff',
    '#357': '#8a2bff',
    '#56': '#8c2fff',
    '#58': '#933ffd',
    '#359': '#683fff',
    '180': '#a064e6',
    '#57': '#b482ff',
    '#356': '#c38dff',
    '#355': '#a590ff',
    '137': '#c8b4e6',
    '#55': '#c0aafd',
    '#353': '#c4adff',
    '#52': '#ddbfff',
    '#53': '#e4dcff',
    '71': '#0000b4',
    '#384': '#0500d0',
    '#83': '#0228ec',
    '508': '#5a46c3',
    '344': '#6662ae',
    '#79': '#1626ff',
    '#82': '#4f34f8',
    '199': '#6464e6',
    '#84': '#5767ff',
    '#78': '#6f6fff',
    '142': '#aaaaf0',
    '#371': '#a3a8ff',
    '709': '#c8c8fa',
    '#372': '#d9dcff',
    '53': '#e6e6fa',
    '713': '#003ca0',
    '120': '#005fbe',
    '#85': '#0049ce',
    '716': '#0064d2',
    '#80': '#0048ff',
    '715': '#3c6edc',
    '714': '#5a91d2',
    '198': '#6478c8',
    '723': '#5082dc',
    '#68': '#447dff',
    '#368': '#448aff',
    '#81': '#486fff',
    '224': '#94a2bd',
    '75': '#64a0f0',
    '#361': '#669efc',
    '197': '#82aae6',
    '710': '#8ca0f0',
    '711': '#aabedc',
    '200': '#91bef5',
    '525': '#8eb4fa',
    '719': '#9bc3f0',
    '712': '#a0bef0',
    '#62': '#a1ceff',
    '500': '#b4d2ff',
    '708': '#dcebfa',
    '#373': '#e0e9fd',
    '502': '#e1f0ff',
    '#76': '#005773',
    '#75': '#007aac',
    '85': '#006eb9',
    '363': '#006ec3',
    '#71': '#0096c7',
    '119': '#0078c8',
    '195': '#006ed2',
    '722': '#008cd2',
    '132': '#00a0dc',
    '721': '#0082e6',
    '#69': '#00a3f7',
    '#369': '#00c6ff',
    '#65': '#00a9ff',
    '79': '#3c8cd2',
    '#67': '#14a9ff',
    '#366': '#29c0f9',
    '143': '#64bed2',
    '68': '#46b4f0',
    '352': '#5ac8e1',
    '#367': '#44a5ff',
    '165': '#5ac8eb',
    '#64': '#50aefd',
    '#72': '#55ccff',
    '196': '#78d2e6',
    '#70': '#6ce5ff',
    '161': '#7dd2f5',
    '#66': '#94eaff',
    '366': '#aad2f0',
    '#63': '#a4d3ff',
    '283': '#afd9f5',
    '174': '#afe1fa',
    '#363': '#abe9ff',
    '191': '#c9dde4',
    '201': '#c3e1fa',
    '720': '#c3e1fb',
    '717': '#c3e1fb',
    '281': '#cde6fa',
    '718': '#d5ecfa',
    '501': '#d7ebfa',
    '63': '#d2f5ff',
    '#61': '#d3eaff',
    '202': '#d7f0ff',
    '61': '#dcf5ff',
    '#395': '#00726a',
    '#392': '#009493',
    '#95': '#009c91',
    '#93': '#01a3a0',
    '729': '#00afaa',
    '727': '#00a5b4',
    '#73': '#00a4b8',
    '116': '#00c8b9',
    '172': '#00dcdc',
    '#370': '#01cddf',
    '183': '#00d7e3',
    '141': '#00d2e6',
    '115': '#00ebc8',
    '118': '#00e1eb',
    '354': '#00f0d7',
    '601': '#90a0a0',
    '144': '#5ae1e6',
    '600': '#98a8aa',
    '353': '#61e8e3',
    '724': '#69e1eb',
    '140': '#87f0eb',
    '117': '#b4faf5',
    '725': '#bef2f3',
    '203': '#ebfcff',
    '#393': '#007150',
    '327': '#008c50',
    '#94': '#00985d',
    '325': '#019879',
    '735': '#00be78',
    '124': '#00dc78',
    '323': '#00e1aa',
    '322': '#41f5be',
    '131': '#64fad2',
    '241': '#aadcc3',
    '#91': '#005e2c',
    '219': '#9bdcaf',
    '190': '#c5e0d1',
    '728': '#c8ebd2',
    '504': '#d2f5dc',
    '730': '#dcffe6',
    '#90': '#007f06',
    '736': '#00aa00',
    '90': '#00be00',
    '#389': '#29f433',
    '89': '#5adc5a',
    '#89': '#51f655',
    '122': '#78fa6e',
    '242': '#b9e6b9',
    '139': '#4bc300',
    '#86': '#89fa19',
    '243': '#cdf5af',
    '731': '#e1fad7',
    '213': '#e6fcdc',
    '740': '#5a6e00',
    '#386': '#7bd300',
    '738': '#aaff00',
    '#388': '#d0f54e',
    '505': '#e3ff5a',
    '121': '#b4ff64',
    '88': '#dcff64',
    '138': '#dcffa0',
    '189': '#d9e6c8',
    '244': '#e6fabe',
    '733': '#ebf7cf',
    '245': '#f0fcd2',
    '246': '#f5ffe6',
    '642': '#968200',
    '643': '#b4a000',
    '104': '#ffdc00',
    '#312': '#ffea00',
    '#10': '#fff200',
    '767': '#ffe600',
    '10': '#ffff00',
    '100': '#f5ff00',
    '101': '#fff500',
    '550': '#e3ca3c',
    '514': '#f5ff5a',
    '#96': '#f3ff6b',
    '513': '#f5ff7d',
    '7': '#fafad2',
    '#07': '#fdfad1',
    '212': '#fffad7',
    '#06': '#fcfadb',
    '746': '#6e3c00',
    '741': '#826400',
    '653': '#965500',
    '777': '#f58200',
    '#15': '#fecb00',
    '15': '#ffcd00',
    '179': '#ffbe00',
    '105': '#ffa000',
    '158': '#ff8700',
    '768': '#ffc600',
    '770': '#ffb400',
    '#14': '#fcd419',
    '#11': '#ffd21a',
    '650': '#c8a862',
    '742': '#e19b50',
    '208': '#e6a550',
    '20': '#ffbe55',
    '207': '#f0b46b',
    '102': '#ffdc5f',
    '#313': '#ffe462',
    '286': '#ffb464',
    '232': '#edbe83',
    '744': '#f8c882',
    '441': '#fac084',
    '204': '#fac387',
    '#09': '#ffcb86',
    '628': '#ffc88c',
    '#13': '#ffd88f',
    '285': '#fccd94',
    '765': '#ffe591',
    '13': '#fcd89b',
    '442': '#fcdcad',
    '188': '#eedabf',
    '205': '#fcd9b1',
    '764': '#fce6b4',
    '103': '#fceacc',
    '763': '#fcf0d2',
    '206': '#fcead6',
    '443': '#fcefdb',
    '444': '#faf3e8',
    '159': '#fffaeb',
    '511': '#963c00',
    '512': '#cc6100',
    '507': '#f85000',
    '781': '#ff5000',
    '19': '#ff4600',
    '164': '#ff3200',
    '135': '#ff5f00',
    '22': '#ff6900',
    '778': '#ff7600',
    '#23': '#ff5a00',
    '780': '#ff6f00',
    '#22': '#ff430a',
    '#19': '#ff390b',
    '#21': '#ff6613',
    '#317': '#ff7418',
    '#20': '#ff871c',
    '#40': '#ff4f1f',
    '#318': '#ff6f29',
    '21': '#ff8c32',
    '652': '#ff8246',
    '25': '#ff6e46',
    '#303': '#ff8a4a',
    '17': '#e68c64',
    '287': '#ffa055',
    '#30': '#ff7a59',
    '651': '#ff9b5f',
    '622': '#ffa064',
    '134': '#faa873',
    '156': '#e1b48c',
    '624': '#ffaa73',
    '8': '#fc9b80',
    '626': '#ffb482',
    '147': '#fcb98c',
    '237': '#fcb292',
    '236': '#fac795',
    '184': '#d3c5bc',
    '187': '#e0c0b3',
    '#04': '#f9b09a',
    '604': '#ffc295',
    '747': '#f5b99f',
    '#01': '#fbb39a',
    '#03': '#fbba9a',
    '776': '#fcbe9b',
    '791': '#f6b8a9',
    '238': '#f5b9aa',
    '775': '#fcc6a4',
    '#304': '#fabca9',
    '790': '#ffb4a5',
    '108': '#fcbea9',
    '#02': '#ffd1ac',
    '773': '#fcc5b2',
    '9': '#fcd7b3',
    '4': '#ffc8b4',
    '774': '#fcd1be',
    '152': '#ffd2c1',
    '151': '#ffcdc3',
    '506': '#ffdace',
    '162': '#fcded8',
    '223': '#fff3e8',
    '#27': '#b00202',
    '789': '#aa3c32',
    '#25': '#e51f00',
    '182': '#f50000',
    '#32': '#ff413c',
    '193': '#f37873',
    '#31': '#ff847f',
    '779': '#fc9885',
    '#331': '#ff9d8d',
    '176': '#ffaaa0',
    '#305': '#f5bab8',
    '109': '#ffb2af',
    '153': '#ffc8c8',
    '749': '#fcd3cd',
    '154': '#ffd5cf',
    '#05': '#ffd7d3',
    '299': '#373536',
    '211': '#67686a',
    '210': '#8e8e8e',
    '225': '#9fa0a2',
    '602': '#a5a5aa',
    '#398': '#b0b4b9',
    '209': '#bababa',
    '270': '#bebebe',
    '275': '#bebebe',
    '603': '#c8cdcd',
    '298': '#cccecd',
    '226': '#f5f2eb',
    '3': '#faf0fa',
    '278': '#f3fff3',
    '279': '#fff3f7',
    '503': '#f4faff',
    '218': '#f5ffff',
    '217': '#f6feff',
    '221': '#f6feff',
    '130': '#ffffff',
    '250': '#ffffff',
    '258': '#ffffff',
    '400': '#ffffff',
    '429': '#ffffff',
    '450': '#ffffff',
    '#100': '#ffffff',
    '#122': '#ffffff',
    '228': '#ffffff',
    '251': '#ffffff',
    '269': '#ffffff',
    '401': '#ffffff',
    '430': '#ffffff',
    '452': '#ffffff',
    '#101': '#ffffff',
    '#124': '#ffffff',
    '229': '#ffffff',
    '252': '#ffffff',
    '402': '#ffffff',
    '432': '#ffffff',
    '460': '#ffffff',
    '#104': '#ffffff',
    '#125': '#ffffff',
    '220': '#ffffff',
    '253': '#ffffff',
    '271': '#ffffff',
    '404': '#ffffff',
    '434': '#ffffff',
    '462': '#ffffff',
    '#00': '#ffffff',
    '#113': '#ffffff',
    '#126': '#ffffff',
    '254': '#ffffff',
    '272': '#ffffff',
    '410': '#ffffff',
    '464': '#ffffff',
    '#114': '#ffffff',
    '#127': '#ffffff',
    '214': '#ffffff',
    '255': '#ffffff',
    '273': '#ffffff',
    '414': '#ffffff',
    '480': '#ffffff',
    '#119': '#ffffff',
    '#132': '#ffffff',
    '215': '#ffffff',
    '256': '#ffffff',
    '274': '#ffffff',
    '416': '#ffffff',
    '481': '#ffffff',
    '#120': '#ffffff',
    '#140': '#ffffff',
    '129': '#ffffff',
    '216': '#ffffff',
    '257': '#ffffff',
    '420': '#ffffff',
    '482': '#ffffff',
    '#121': '#ffffff',
    '#160': '#ffffff',
# HTML standard colours
    'AliceBlue': '#F0F8FF',
    'AntiqueWhite': '#FAEBD7',
    'Aqua': '#00FFFF',
    'Aquamarine': '#7FFFD4',
    'Azure': '#F0FFFF',
    'Beige': '#F5F5DC',
    'Bisque': '#FFE4C4',
    'Black': '#000000',
    'BlanchedAlmond': '#FFEBCD',
    'Blue': '#0000FF',
    'BlueViolet': '#8A2BE2',
    'Brown': '#A52A2A',
    'BurlyWood': '#DEB887',
    'CadetBlue': '#5F9EA0',
    'Chartreuse': '#7FFF00',
    'Chocolate': '#D2691E',
    'Coral': '#FF7F50',
    'CornflowerBlue': '#6495ED',
    'Cornsilk': '#FFF8DC',
    'Crimson': '#DC143C',
    'Cyan': '#00FFFF',
    'DarkBlue': '#00008B',
    'DarkCyan': '#008B8B',
    'DarkGoldenrod': '#B8860B',
    'DarkGray': '#A9A9A9',
    'DarkGreen': '#006400',
    'DarkKhaki': '#BDB76B',
    'DarkMagenta': '#8B008B',
    'DarkOliveGreen': '#556B2F',
    'DarkOrange': '#FF8C00',
    'DarkOrchid': '#9932CC',
    'DarkRed': '#8B0000',
    'DarkSalmon': '#E9967A',
    'DarkSeaGreen': '#8FBC8F',
    'DarkSlateBlue': '#483D8B',
    'DarkSlateGray': '#2F4F4F',
    'DarkTurquoise': '#00CED1',
    'DarkViolet': '#9400D3',
    'DeepPink': '#FF1493',
    'DeepSkyBlue': '#00BFFF',
    'DimGray': '#696969',
    'DodgerBlue': '#1E90FF',
    'FireBrick': '#B22222',
    'FloralWhite': '#FFFAF0',
    'ForestGreen': '#228B22',
    'Fuchsia': '#FF00FF',
    'Gainsboro': '#DCDCDC',
    'GhostWhite': '#F8F8FF',
    'Gold': '#FFD700',
    'Goldenrod': '#DAA520',
    'Gray': '#808080',
    'Green': '#008000',
    'GreenYellow': '#ADFF2F',
    'Honeydew': '#F0FFF0',
    'HotPink': '#FF69B4',
    'IndianRed': '#CD5C5C',
    'Indigo': '#4B0082',
    'Ivory': '#FFFFF0',
    'Khaki': '#F0E68C',
    'Lavender': '#E6E6FA',
    'LavenderBlush': '#FFF0F5',
    'LawnGreen': '#7CFC00',
    'LemonChiffon': '#FFFACD',
    'LightBlue': '#ADD8E6',
    'LightCoral': '#F08080',
    'LightCyan': '#E0FFFF',
    'LightGoldenrodYellow': '#FAFAD2',
    'LightGreen': '#90EE90',
    'LightGrey': '#D3D3D3',
    'LightPink': '#FFB6C1',
    'LightSalmon': '#FFA07A',
    'LightSeaGreen': '#20B2AA',
    'LightSkyBlue': '#87CEFA',
    'LightSlateGray': '#778899',
    'LightSteelBlue': '#B0C4DE',
    'LightYellow': '#FFFFE0',
    'Lime': '#00FF00',
    'LimeGreen': '#32CD32',
    'Linen': '#FAF0E6',
    'Magenta': '#FF00FF',
    'Maroon': '#800000',
    'MediumAquamarine': '#66CDAA',
    'MediumBlue': '#0000CD',
    'MediumOrchid': '#BA55D3',
    'MediumPurple': '#9370DB',
    'MediumSeaGreen': '#3CB371',
    'MediumSlateBlue': '#7B68EE',
    'MediumSpringGreen': '#00FA9A',
    'MediumTurquoise': '#48D1CC',
    'MediumVioletRed': '#C71585',
    'MidnightBlue': '#191970',
    'MintCream': '#F5FFFA',
    'MistyRose': '#FFE4E1',
    'Moccasin': '#FFE4B5',
    'NavajoWhite': '#FFDEAD',
    'Navy': '#000080',
    'OldLace': '#FDF5E6',
    'Olive': '#808000',
    'OliveDrab': '#6B8E23',
    'Orange': '#FFA500',
    'OrangeRed': '#FF4500',
    'Orchid': '#DA70D6',
    'PaleGoldenrod': '#EEE8AA',
    'PaleGreen': '#98FB98',
    'PaleTurquoise': '#AFEEEE',
    'PaleVioletRed': '#DB7093',
    'PapayaWhip': '#FFEFD5',
    'PeachPuff': '#FFDAB9',
    'Peru': '#CD853F',
    'Pink': '#FFC0CB',
    'Plum': '#DDA0DD',
    'PowderBlue': '#B0E0E6',
    'Purple': '#800080',
    'Red': '#FF0000',
    'RosyBrown': '#BC8F8F',
    'RoyalBlue': '#4169E1',
    'SaddleBrown': '#8B4513',
    'Salmon': '#FA8072',
    'SandyBrown': '#F4A460',
    'SeaGreen': '#2E8B57',
    'Seashell': '#FFF5EE',
    'Sienna': '#A0522D',
    'Silver': '#C0C0C0',
    'SkyBlue': '#87CEEB',
    'SlateBlue': '#6A5ACD',
    'SlateGray': '#708090',
    'Snow': '#FFFAFA',
    'SpringGreen': '#00FF7F',
    'SteelBlue': '#4682B4',
    'Tan': '#D2B48C',
    'Teal': '#008080',
    'Thistle': '#D8BFD8',
    'Tomato': '#FF6347',
    'Turquoise': '#40E0D0',
    'Violet': '#EE82EE',
    'Wheat': '#F5DEB3',
    'White': '#FFFFFF',
    'WhiteSmoke': '#F5F5F5',
    'Yellow': '#FFFF00',
    'YellowGreen': '#9ACD32'
}
