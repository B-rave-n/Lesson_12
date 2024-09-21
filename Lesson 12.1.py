import re

def delete_html_tags(file_for_cleaned, clean_file):
    pattern = r'<[^>]+>'
    file_1 = f'{file_for_cleaned}'
    file_2 = f'{clean_file}'
    with open(file_1, 'r') as file:
        content = file.read()
        cleaned_content = re.sub(pattern,'', content)
        lst = cleaned_content.split('\n')
        result = []
        for i in lst:
            if i.strip() != '':
                result.append(i)
    with open(file_2, 'w') as cleaned:
        cleaned.write('\n'.join(result))

delete_html_tags('draft.html', 'cleaned.txt')