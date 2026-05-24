from utils.config import load_config, DEFAULT_CONFIG_PATH

print("配置文件路径：",DEFAULT_CONFIG_PATH)
print("文件存在吗？",DEFAULT_CONFIG_PATH.exists())



config_test=load_config()
print(config_test["base_url"])
print(config_test["api_base_url"])
print(config_test["ui_base_url"])
print(config_test["timeout_seconds"])
print(config_test["headless"])
