from horizon import tables

from tasa.store import connection


class RestartWorker(tables.Action):
    name = 'restart'
    verbose_name = 'Restart Worker'
    data_type_singular = 'Worker'
    action_present = 'restart'
    requires_input = False
    classes = ('btn-warning',)

    def handle(self, data_table, request, object_ids):
        # Send a restart signal
        connection.publish('control', 'restart')


class WorkerTable(tables.DataTable):
    hostname = tables.Column('hostname')

    class Meta:
        name = 'workers'
        verbose_name = 'Workers'
        table_actions = (RestartWorker,)
