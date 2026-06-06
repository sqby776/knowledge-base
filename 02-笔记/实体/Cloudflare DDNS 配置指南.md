# Cloudflare DDNS 配置指南

## 目标
自动更新域名 `sqby.cc.cd` 的 IPv6 地址记录

## 当前状态

| 项目 | 值 |
|------|-----|
| 域名 | `sqby.cc.cd` |
| DNS 服务商 | Cloudflare |
| 当前 AAAA 记录 | `2409:8a4b:77ba:8ba0:59cd:c222:bad1:ea08` |
| 本机当前 IPv6 | `2409:8a4b:77ba:8ba0:1420:c8de:55dd:214e` |
| **问题** | DNS 记录未更新，外部访问失败 |

---

## 配置步骤

### 步骤 1：获取 Zone ID

1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/)
2. 选择域名 `sqby.cc.cd`
3. 在右侧信息面板中找到 **Zone ID**
4. 复制 Zone ID（32 位字符串）

### 步骤 2：创建 API Token

1. 点击右上角头像 → **My Profile** → **API Tokens**
2. 点击 **Create Token**
3. 选择 **Edit zone DNS** 模板（或自定义）
4. 配置权限：
   - `Zone > DNS > Edit` ✅
5. 配置资源范围：
   - **Account Resources**: 选择 `sqby.cc.cd`
6. 点击 **Continue to summary**
7. 点击 **Create Token**
8. **复制 Token**（只显示一次！）

### 步骤 3：配置脚本

编辑脚本 `~/workspace/scripts/cloudflare-ddns.sh`：

```bash
CF_API_TOKEN="你的_API_TOKEN"
CF_ZONE_ID="你的_ZONE_ID"
```

### 步骤 4：测试运行

```bash
chmod +x ~/workspace/scripts/cloudflare-ddns.sh
~/workspace/scripts/cloudflare-ddns.sh
```

### 步骤 5：设置定时任务

```bash
crontab -e
```

添加以下行（每 5 分钟检查一次）：

```
*/5 * * * * ~/workspace/scripts/cloudflare-ddns.sh >> ~/workspace/data/ddns.log 2>&1
```

### 步骤 6：验证更新

```bash
# 查看 DNS 记录
dig sqby.cc.cd AAAA +short

# 查看更新日志
tail -20 ~/workspace/data/ddns.log
```

---

## 常见问题

### Q: 找不到 Zone ID？
A: 在 Cloudflare 域名设置页面，Zone ID 显示在右侧信息面板顶部。

### Q: API Token 无效？
A: 检查 Token 权限是否包含 `Zone > DNS > Edit`。

### Q: 找不到 AAAA 记录？
A: 在 Cloudflare DNS 设置中手动添加一条 AAAA 记录：
- 类型: `AAAA`
- 名称: `sqby.cc.cd`
- IPv6 地址: 任意地址（脚本会更新）
- TTL: 自动

### Q: 脚本运行成功但 DNS 未更新？
A: Cloudflare DNS 传播需要 1-5 分钟，稍后再次验证。

---

## 备选方案：Cloudflare Tunnel

如果 IPv6 不稳定，可以考虑使用 Cloudflare Tunnel：

1. 安装 `cloudflared`
2. 创建 Tunnel
3. 配置域名路由到本地服务

优点：
- 无需公网 IP
- 无需 DDNS
- 更安全（无需开放端口）

缺点：
- 需要运行 `cloudflared` 进程
- 国内访问可能较慢

---

## 相关文档

- Cloudflare API 文档: https://api.cloudflare.com/
- DDNS 脚本: `~/workspace/scripts/cloudflare-ddns.sh`
- 更新日志: `~/workspace/data/ddns.log`
