{{- define "my-app.name" -}}
{{- .Chart.Name | lower -}}
{{- end -}}

{{- define "my-app.fullname" -}}
{{- include "my-app.name" . }}-{{ .Release.Name | lower }}
{{- end -}}

{{- define "my-app.redisFullname" -}}
{{- include "my-app.name" . }}-redis-{{ .Release.Name | lower }}
{{- end -}}

{{- define "my-app.prometheusFullname" -}}
{{- include "my-app.name" . }}-prometheus-{{ .Release.Name | lower }}
{{- end -}}