from scripts import tier3_corpus_figure


def test_dissociation_figure_uses_pure_envelope_channel() -> None:
    assert tier3_corpus_figure.SECOND_PANEL_COLUMN == "A_mean"
