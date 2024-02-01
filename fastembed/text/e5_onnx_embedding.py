from typing import Type, List, Dict, Any

import numpy as np

from fastembed.text.onnx_embedding import OnnxTextEmbedding, OnnxTextEmbeddingWorker, EmbeddingWorker
from fastembed.text.onnx_models import supported_multilingual_e5_models


class E5OnnxEmbedding(OnnxTextEmbedding):

    @classmethod
    def _get_worker_class(cls) -> Type["EmbeddingWorker"]:
        return E5OnnxEmbeddingWorker

    @classmethod
    def list_supported_models(cls) -> List[Dict[str, Any]]:
        """Lists the supported models.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing the model information.
        """
        return supported_multilingual_e5_models

    def _preprocess_onnx_input(self, onnx_input: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Preprocess the onnx input.
        """
        onnx_input.pop("token_type_ids", None)
        return onnx_input


class E5OnnxEmbeddingWorker(OnnxTextEmbeddingWorker):
    def init_embedding(
            self,
            model_name: str,
            cache_dir: str,
    ) -> E5OnnxEmbedding:
        return E5OnnxEmbedding(model_name=model_name, cache_dir=cache_dir, threads=1)
