from datetime import datetime, timedelta, timezone

import boto3
ec2 = boto3.resource('ec2')

# List(ec2.Snapshot)
snapshots = ec2.snapshots.filter(OwnerIds=['self'])

for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=0)
    if delete_time > start_time:
        print('fmt_start_time = {} And delete_time = {}'.format(start_time, delete_time))
        #snapshot.delete()
        #print('Snapshot with Id = {} is deleted '.format(snapshot.snapshot_id))