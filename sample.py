from POS.POSTagger import POSTagger

pos_tagger = POSTagger("/home/hassan/PycharmProjects/perpos_git/model/perpos.model")
print(pos_tagger.parse("به گزارش گروه بین الملل خبرگزاری فارس، «بشار اسد» رئیس جمهور سوریه در جمع روزنامه نگاران روس گفت که هر گونه عملیات نظامی در سوریه بدون موافقت مقامات این کشور، تجاوز است؛ چه در رقه باشد یا در سایر مناطق.".split()))
