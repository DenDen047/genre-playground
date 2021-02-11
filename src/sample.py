import pickle

from genre import GENRE


if __name__ == '__main__':
    # load the model
    model = GENRE.from_pretrained(
        data_name_or_path="/models",
        model_name_or_path="fairseq_entity_disambiguation_aidayago"
    ).eval()

    # prepare dataset
    with open("/data/kilt_titles_trie.pkl", "rb") as f:
        trie = pickle.load(f)

    def prefix_allowed_tokens_fn(batch_id, sent):
        return trie.get(sent.tolist())