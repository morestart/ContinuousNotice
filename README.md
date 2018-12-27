# HomeAssistant 前端提醒组件(适配lovelace-ui)

## 使用方法：

- 将notice.py放于`homeassistant\components`下

## 配置内容:

configuration文件下写入以下内容
```yaml
notice:
  time: 推送时间间隔
  title: 推送标题
  message: 推送信息
```
更新时间默认为启动后一天一次,可通过time选项来调整更新时间,时间单位为秒

## 举个🌰

```yaml
notice:
  title: hello
  time: 60
  message: 最高温度:{{states("sensor.heweather_tmp_max")}}， 最低温度:{{states("sensor.heweather_tmp_min")}}，
        今日穿衣建议:{{states.sensor.heweather_drsg.attributes.生活建议}}
```

## 更新日志
- 首次提交