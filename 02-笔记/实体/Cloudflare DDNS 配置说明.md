# Cloudflare DDNS 配置说明

## 1. 获取 Zone ID

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 选择你的域名 `sqby.cc.cd`
3. 在右侧信息面板中找到 **Zone ID**
4. 复制 Zone ID（类似 `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

## 2. 创建 API Token

1. 点击右上角头像 → **My Profile** → **API Tokens**
2. 点击 **Create Token**
3. 选择 **Edit zone DNS** 模板
4. 在 **Permissions** 中确认有 `Zone > DNS > Edit`
5. 在 **Account Resources** 中选择你的域名 `sqby.cc.cd`
6. 点击 **Continue to summary**
7. 点击 **Create Token**
8. 复制 Token（只显示一次，请妥善保存）

## 3. 配置脚本

编辑脚本中的配置区域：

```bash
CF_API_TOKEN="你的_API_TOKEN"
CF_ZONE_ID="你的_ZONE_ID"
```

或者设置环境变量：

```bash
export CF_API_TOKEN="你的_API_TOKEN"
export CF_ZONE_ID="你的_ZONE_ID"
```

## 4. 测试运行

```bash
chmod +x ~/workspace/scripts/cloudflare-ddns.sh
~/workspace/scripts/cloudflare-ddns.sh
```

## 5. 设置定时任务

```bash
crontab -e
```

添加以下行（每 5 分钟检查一次）：

```
*/5 * * * * CF_API_TOKEN="你的_TOKEN" CF_ZONE_ID="你的_ZONE_ID" ~/workspace/scripts/cloudflare-ddns.sh >> ~/workspace/data/ddns.log 2>&1
```

## 6. 验证更新

```bash
dig sqby.cc.cd AAAA +short
```

应该显示你当前的 IPv6 地址。
