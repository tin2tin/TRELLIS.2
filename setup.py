from setuptools import setup, find_packages

setup(
    name="trellis",
    version="0.1.0",
    description="TRELLIS.2: Large-scale Autoregressive Model for 3D Asset Generation",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "timm",
        "transformers",
        "accelerate",
        "diffusers",
        "einops",
        "scipy",
        "tqdm",
        "imageio",
        "imageio-ffmpeg",
        "trimesh",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
)
