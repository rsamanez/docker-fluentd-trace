# Ejemplo para implementar Fluentd-Trace escuchando en un puerto UDP
```
docker build -t fluentd-udp .
docker run --rm -p 5160:5160/udp --name fluentd-original fluentd-udp
```
Enviar un Test usando el ejemplo con Python
```
python3 send_udp.py
```
Pare verificar el envio Ingresar a la cuenta de NewRelic - Insights y colocar la siguiente Query
```
SELECT * FROM Span
```

## Para enviar por TCP
renombrar:
```
mv fluent.comf.tcp fluent.conf
docker build -t fluentd-tcp .
docker run --rm -p 5170:5170 --name fluentd-original fluentd-tcp
```
probar con
```
echo '{"trace.id":"1234533-PYTHON","id":"tcp-py"}' | netcat 0.0.0.0 5170
```
Terminar con Control+C

