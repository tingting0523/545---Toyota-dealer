# 545---Toyota-dealer

To connect to Cassandra, in project directory, run: docker run --rm --network cassandra -v "$(pwd)/cass_connection.cql" -e CQLSH_HOST=cassandra -e CQLSH_PORT=9042 -e CQLVERSION=3.4.6 nuvo/docker-cqlsh


System design link: https://lucid.app/lucidspark/e81a8ed4-9af8-4208-b286-d6cead356e7f/edit?viewport_loc=-312%2C269%2C3061%2C1656%2C0_0&invitationId=inv_e7929f4d-66dd-40a0-9368-eec3bce8760e
