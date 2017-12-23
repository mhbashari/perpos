# Cross-platform Parts-of-Speech tagger

This is another persian POS tagger can be used in any operating system.

## Sample
    from POS.POSTagger import POSTagger

    pos_tagger = POSTagger("model/perpos.model")
    tokens = "حلقه محاصره تروریست‌ها در جنوب سوریه تنگتر شد".split()
    pos_tagger.parse(tokens)

## Evaluation

                    precision   recall      f1-score   support

          N         0.985       0.970       0.977       186585
          P         0.998       0.998       0.998       89450
          V         0.999       0.999       0.999       87762
        ADV         0.976       0.972       0.974       15983
       ADVe         0.988       0.978       0.983       1053
        RES         0.989       0.992       0.991       2784
       RESe         1.000       0.989       0.994       174
        DET         0.973       0.977       0.975       19786
       DETe         0.960       0.970       0.965       2156
         AJ         0.978       0.975       0.977       61526
        AJe         0.949       0.964       0.957       19919
         CL         0.932       0.918       0.925       1892
        INT         1.000       1.000       1.000       73
       CONJ         0.996       0.997       0.997       74796
      CONJe         1.000       1.000       1.000       82
      POSTP         1.000       1.000       1.000       13174
        PRO         0.973       0.974       0.973       23094
       PROe         0.878       0.579       0.698       273
        NUM         0.988       0.992       0.990       24864
       NUMe         0.932       0.918       0.925       2519
       PUNC         1.000       1.000       1.000       84088
         Ne         0.970       0.985       0.977       163760
         Pe         0.986       0.992       0.989       10004
      --------------------------------------------------------
    avg/total       0.985      0.985        0.985       885797
    
 