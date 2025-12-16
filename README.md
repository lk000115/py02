- vscode 配置识别python虚拟环境

```python
在settings.json中添加
"python.venvPath": '虚拟环境的绝对路径'   #  如: 'd:\\venv'

##  使用conda配置python虚拟环境
  初始化   conda init cmd.exe  或 powershell

创建虚拟环境,虚拟环境名AC
conda create -n ac python=3.11
激活基础conda虚拟环境 base
conda activate
激活虚拟环境ac
conda activate  ac

conda env list   列出虚拟环境列表

查看当前环境中的所有包
conda list

# py02
python数据分析--20251028
