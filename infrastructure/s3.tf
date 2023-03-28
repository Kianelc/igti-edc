resource "aws_s3_bucket" "dl" {
    # Parâmetros de configuração do recurso escolhido
    bucket = "${var.base_bucket_name}_${var.ambiente}_${var.numero_conta}"
    acl = "private"

    tags = {
        IES = "IGTI"
        CURSO = "EDC"
    }

    server_side_encryption_configuration {
        rule {
            apply_server_side_encryption_by_default {
                sse_algorithm = "AES256"
            }
        }
    }
}