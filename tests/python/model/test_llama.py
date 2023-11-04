# pylint: disable=invalid-name,missing-docstring
import pytest

from mlc_chat.compiler import MODEL_PRESETS, MODELS


@pytest.mark.parametrize("model_name", ["llama2_7b", "llama2_13b", "llama2_70b"])
def test_llama2_creation(model_name: str):
    model = MODELS["llama"].model(MODEL_PRESETS[model_name])
    mod, named_params = model.export_tvm(
        spec=model.get_default_spec(),  # type: ignore
    )
    mod.show(black_format=False)
    for name, param in named_params:
        print(name, param.shape, param.dtype)


if __name__ == "__main__":
    test_llama2_creation("llama2_7b")
    test_llama2_creation("llama2_13b")
    test_llama2_creation("llama2_70b")
