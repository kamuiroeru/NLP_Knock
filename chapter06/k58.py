from k54 import load_xml

# collapsed-dependenciesは2番目
dependencies = [sentences['dependencies'][1] for sentences in load_xml()['root']['document']['sentences']['sentence']]

for dep in dependencies:
    dd, dg = dep['dependent'], dep['governor']  # 文字数削減
