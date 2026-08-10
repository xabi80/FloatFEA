"""Reader, validator and schema versioning for the .flr load interchange.

Schema: docs/load-interchange-v1.md. The reader REJECTS bad records; it never
warns and continues. A structure analysed under misinterpreted loads is the
failure mode this project exists to prevent.
"""
