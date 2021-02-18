import pickle
import numpy as np
from pprint import pprint
import logging

from genre import GENRE
from genre.entity_linking import get_end_to_end_prefix_allowed_tokens_fn_fairseq


if __name__ == '__main__':
    # print('load the trie ...', end='', flush=True)
    # with open("data/kilt_titles_trie.pkl", "rb") as f:
    #     trie = pickle.load(f)
    # print('ok')

    # def prefix_allowed_tokens_fn(batch_id, sent):
    #     return trie.get(sent.tolist())

    # load the model
    model = GENRE.from_pretrained("/models/fairseq_e2e_entity_linking_aidayago.tar.gz").eval()

    sentences = ["In 1921, Einstein received a Nobel Prize."]
    prefix_allowed_tokens_fn = get_end_to_end_prefix_allowed_tokens_fn_fairseq(model, sentences)
    result = model.sample(
        sentences,
        prefix_allowed_tokens_fn=prefix_allowed_tokens_fn,
    )

    pprint(result)