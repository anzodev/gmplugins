import setuptools


setuptools.setup(
    name="gmplugins",
    version="1.0",
    author="anzodev",
    packages=["gmplugins"],
    entry_points={
        "console_scripts": [
            "gm-battery=gmplugins.battery:main",
            "gm-cmc-prices=gmplugins.cmc_prices:main",
            "gm-ip-address=gmplugins.ip_address:main",
            "gm-load-average=gmplugins.load_average:main",
            "gm-memory=gmplugins.memory:main",
            "gm-net-traffic=gmplugins.net_traffic:main",
            "gm-time=gmplugins.time:main",
            "gm-weather=gmplugins.weather:main",
        ]
    },
    install_requires=["psutil>=5.8.0", "requests>=2.26.0"],
    python_requires=">=3.6",
)
