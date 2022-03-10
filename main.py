#Software By AwesomeWithRex


def read_file(filename):
    with open(filename) as f:
        filename = f.readlines()
    return filename

def get_template():
    template = ''
    with open('template.html', 'r') as f:
        template = f.readlines()
    return template

def put_in_body(file, template):
    count = 0
    body_tag = 0
    for i in template:
        count += 1
        if '|b|' in i:
            body_tag = count - 1
    
    text_to_append = ""
    for line in file:
        text_to_append += line

    formatted_text = ""
    for word in text_to_append:
        formatted_text += word
        if '\n' in word:
            formatted_text += word.replace('\n', '<br/>\t')    

    template[body_tag] = template[body_tag].replace('|b|', formatted_text)

    for i in template:
        print(i)


    return template 

def save_template(name_of_doc, saved_doc_file):
    with open(name_of_doc, 'w') as f:
        f.writelines(saved_doc_file)
    

def put_in_title():
    pass


def main():
    content = read_file('text.txt')
    template = get_template()
    formatted_template = put_in_body(content, template)

    save_template('the.html',formatted_template)

if __name__=='__main__':
    main()
