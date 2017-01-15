from k54 import load_xml
import re

parse_strings = [sentences['parse'] for sentences in load_xml()['root']['document']['sentences']['sentence']]

for ps in parse_strings:
    start = 0  # (NP の開始位置を保存
    while len(ps) > start:
        start += 1

        if ps[start:start + 3] == '(NP':  # (NPが見つかった時

            # 終端位置endを探す、countは()の数をカウント
            end, count = start + 1, 1
            while count:  # count が0以上の間
                if ps[end] == '(':
                    count += 1
                elif ps[end] == ')':
                    count -= 1
                end += 1

            outList = []
            # 先頭と終端がわかったので、中に入っている単語だけ抜き取る
            for word in ps[start:end + 1].split(' '):
                if word and word[-1] == ')':
                    outList.append(word.replace(')', ''))

            outStr = re.sub(r' ([,.;:?!])', r'\1', ' '.join(outList))  # カンマやピリオドの前の空白を削除
            outStr = outStr.replace('-LRB- ', '(').replace(' -RRB-', ')')  # ()を復元

            print(outStr)
