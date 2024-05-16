import requests
import yaml

URL = "https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml"

data = yaml.safe_load(requests.get(URL).text)

lang_names = list(data.keys())

aliases = []
for lang_data in data.values():
    extensions = lang_data.get('aliases', [])
    aliases.extend(extensions)

language_options = [*lang_names, *aliases]
language_options.sort()
print('  "'+'" |\n  "'.join(language_options)+'"')