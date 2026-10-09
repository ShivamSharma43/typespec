# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from pygen.codegen.models import CodeModel

OPTIONS = {
    "show-send-request": True,
    "builders-visibility": "public",
    "show-operations": True,
    "models-mode": "dpg",
}


def get_code_model(clients):
    return CodeModel({"clients": clients, "namespace": "employee.management"}, options=OPTIONS)


def test_client_namespace_types_without_clients_models_or_enums():
    # e.g. a service whose only interface is empty: https://github.com/microsoft/typespec/issues/7835
    code_model = get_code_model([])

    client_namespace_types = code_model.client_namespace_types

    assert sorted(client_namespace_types) == ["", "employee", "employee.management"]
    for client_namespace_type in client_namespace_types.values():
        assert not client_namespace_type.clients
        assert not client_namespace_type.models
        assert not client_namespace_type.enums
        assert not client_namespace_type.operation_groups
    assert not code_model.has_subnamespace


def test_client_namespace_types_with_client():
    code_model = get_code_model(
        [
            {
                "name": "client",
                "namespace": "employee.management",
                "clientNamespace": "employee.management",
                "moduleName": "client",
                "parameters": [],
                "url": "",
                "operationGroups": [],
            }
        ]
    )

    client_namespace_types = code_model.client_namespace_types

    assert sorted(client_namespace_types) == ["", "employee", "employee.management"]
    assert [c.name for c in client_namespace_types["employee.management"].clients] == ["client"]
