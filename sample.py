from POS.POSTagger import POSTagger

pos_tagger = POSTagger("model/perpos.model")
tokens = "حلقه محاصره تروریست‌ها در جنوب سوریه تنگتر شد".split()
pos_tagger.parse(tokens)
