import pickle

from POS.crf_pos_feature_helper import token2features


class POSTagger:
    def __init__(self, model_path):
        self.model_path = model_path
        self.crf = pickle.load(open(model_path, "rb"))

    def parse(self, token_stream):
        return self.parse_sentences([token_stream])[0]

    def parse_sentences(self, list_of_token_stream):
        X_test = [token2features(s) for s in list_of_token_stream]
        y_pred = self.crf.predict(X_test)
        out = []
        for x_sent, y_pred in zip(list_of_token_stream, y_pred):
            out.append(list(zip(x_sent, y_pred)))
        return out
