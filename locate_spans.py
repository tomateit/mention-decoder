import spacy_alignments as tokenizations

def locate_spans(decoded_inputs, samples) -> list[tuple[int, int]]:
    """
    Given a lists of tokens and substrings, find substrings' locations
    """
    entity_spans = []
    for sample, decoded_tokens in zip(samples, decoded_inputs):
        a2b, b2a = tokenizations.get_alignments(list(sample.text), decoded_tokens)
        direct_slice = a2b[sample.span[0]:sample.span[1]] # [[0],[1],[1],[2]]
        flat_slice = [a[0] for a in direct_slice if a] # [0, 1, 1, 2]
        try:
            span_start, span_end = min(flat_slice), max(flat_slice)
        except ValueError:
            # Some entities do not have matching alignment (e.g. that contain UNK tokens)
            entity_spans.append(None)
        else:
            entity_spans.append((span_start, span_end))
    return entity_spans