
from typing import NamedTuple

from kfp.dsl import pipeline
from kfp.dsl import component
from kfp import compiler

@component() 
def concat(a: str, b: str) -> str:
    return a + b

@component
def reverse(a: str) -> NamedTuple("outputs", [("before", str), ("after", str)]):
    return a, a[::-1]

@pipeline(name="mlops-pipeline")
def basic_pipeline(a: str='stres', b: str='sed'):
    concat_task = concat(a=a, b=b)
    reverse_task = reverse(a=concat_task.output)

if __name__ == '__main__':
    compiler.Compiler().compile(pipeline_func=basic_pipeline, package_path="pipeline.yaml")
