# Security Rules

## 1. Environment Desensitization
This repository (`E:\_projects\_tech-analysis`) is an open-source environment. Any sensitive information (such as passwords, secret keys, private IP addresses, database credentials, or proprietary internal domains) MUST be desensitized or masked (e.g., using `***`) before being committed or written to any file in this directory.

## 文档目录规范（z-readme vs z-docs）

- **所有生成的文档统一写入 z-readme/ 文件夹**（包括架构设计、业务描述、技术方案、操作手册、分析报告等，统一使用中文并添加 YYYYMMDDHHMM_ 时间戳前缀）。
- **z-docs/ 仅作为原始需求文档使用**（存放用户提供的原始需求、外部参考资料与输入规范，禁止将新生成的文档写入 z-docs/）。
