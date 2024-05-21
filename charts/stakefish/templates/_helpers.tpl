{{- define "stakefish.name" -}}
{{- .Chart.Name | lower -}}
{{- end -}}

{{- define "stakefish.fullname" -}}
{{- include "stakefish.name" . }}-{{ .Release.Name | lower }}
{{- end -}}
