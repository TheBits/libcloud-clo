# clo.ru libcloud driver

# Поддерживаемые методы Compute

## NodeDriver

### Параметры

| Параметр    | Поддержка |
| ----------- | --------- |
| key         |           |
| secret      |           |
| secure      |           |
| host        |           |
| port        |           |
| api_version |           |
| region      |           |

### Управление нодами

| Метод                                                                                                                                | Поддержка |
| ------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| [create_node](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.create_node)               | #15       |
| [deploy_node](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.deploy_node)               |           |
| [destroy_node](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.destroy_node)             | #19       |
| [features](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.features)                     |           |
| [list_nodes](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.list_nodes)                 | #20       |
| [reboot_node](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.reboot_node)               | #21       |
| [start_node](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.start_node)                 | #21       |
| [stop_node](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.stop_node)                   | #21       |
| [wait_until_running](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.wait_until_running) |           |

### Управление образами

| Метод                                                                                                                    | Поддержка |
| ------------------------------------------------------------------------------------------------------------------------ | --------- |
| [copy_image](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.copy_image)     |           |
| [create_image](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.create_image) |           |
| [delete_image](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.delete_image) |           |
| [get_image](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.get_image)       |           |
| [list_images](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.list_images)   | done      |

### Управление дисками

| Метод                                                                                                                                          | Поддержка |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [attach_volume](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.attach_volume)                     |           |
| [create_volume_snapshot](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.create_volume_snapshot)   |           |
| [create_volume](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.create_volume)                     |           |
| [destroy_volume_snapshot](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.destroy_volume_snapshot) |           |
| [destroy_volume](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.destroy_volume)                   |           |
| [detach_volume](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.detach_volume)                     |           |
| [list_volume_snapshots](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.list_volume_snapshots)     |           |
| [list_volumes](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.list_volumes)                       |           |

### Управление SSH ключами

| Метод                                                                                                                                                  | Поддержка |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| [create_key_pair](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.create_key_pair)                         |           |
| [delete_key_pair](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.delete_key_pair)                         |           |
| [get_key_pair](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.get_key_pair)                               |           |
| [import_key_pair_from_file](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.import_key_pair_from_file)     |           |
| [import_key_pair_from_string](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.import_key_pair_from_string) |           |
| [list_key_pairs](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.list_key_pairs)                           |           |

### Остальные

| Метод                                                                                                                        | Поддержка |
| ---------------------------------------------------------------------------------------------------------------------------- | --------- |
| [list_locations](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.list_locations) |           |
| [list_sizes](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.NodeDriver.list_sizes)         |           |

## Методы Node

### Параметры

| Параметр    | Поддержка |
| ----------- | --------- |
| id          |           |
| name        |           |
| state       |           |
| public_ips  |           |
| private_ips |           |
| driver      |           |
| size        |           |
| image       |           |
| created_at  |           |
| extra       |           |

### Методы

| Метод                                                                                                        | Поддержка |
| ------------------------------------------------------------------------------------------------------------ | --------- |
| [destroy](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.Node.destroy)     |           |
| [reboot](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.Node.reboot)       |           |
| [start](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.Node.start)         |           |
| [stop_node](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.Node.stop_node) |           |

## Методы NodeSize

### Параметры

| Параметр  | Поддержка |
| --------- | --------- |
| id        |           |
| name      |           |
| ram       |           |
| disk      |           |
| bandwidth |           |
| price     |           |
| driver    |           |
| extra     |           |

## NodeImage

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| id       |           |
| name     |           |
| driver   |           |
| extra    |           |

## NodeLocation

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| id       |           |
| name     |           |
| country  |           |
| driver   |           |
| extra    |           |

## NodeAuthSSHKey

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| pubkey   |           |

## NodeAuthPassword

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| password |           |

## StorageVolume

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| id       |           |
| name     |           |
| size     |           |
| driver   |           |
| state    |           |
| extra    |           |

### Методы

| Метод                                                                                                                           | Поддержка |
| ------------------------------------------------------------------------------------------------------------------------------- | --------- |
| [attach](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.StorageVolume.attach)                 |           |
| [destroy](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.StorageVolume.destroy)               |           |
| [detach](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.StorageVolume.detach)                 |           |
| [list_snapshots](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.StorageVolume.list_snapshots) |           |
| [snapshot](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.StorageVolume.snapshot)             |           |

## VolumeSnapshot

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| id       |           |
| driver   |           |
| size     |           |
| extra    |           |
| created  |           |
| state    |           |
| name     |           |

### Методы

| Метод                                                                                                              | Поддержка |
| ------------------------------------------------------------------------------------------------------------------ | --------- |
| [destroy](https://libcloud.readthedocs.io/en/stable/compute/api.html#libcloud.compute.base.VolumeSnapshot.destroy) |           |

## KeyPair

| Параметр    | Поддержка |
| ----------- | --------- |
| name        |           |
| fingerprint |           |
| public_key  |           |
| private_key |           |
| extra       |           |

## NodeState

Указаны возомжно состояния

| Состояние | Поддержка |
| --------- | --------- |
| RUNNING   |           |

# DNS

## DNSDriver

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| key      |           |
| secret   |           |
| secure   |           |
| host     |           |
| port     |           |

### Методы

| Метод                                                                                                                                             | Поддержка | Примечание |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------- |
| [create_record](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.create_record)                                 |           |            |
| [create_zone](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.create_zone)                                     | #3        |            |
| [delete_record](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.delete_record)                                 | #7        |            |
| [delete_zone](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.delete_zone)                                     | #4        |            |
| [list_records](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.list_records)                                   |           |            |
| [list_zones](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.list_zones)                                       | #2        |            |
| [iterate_records](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.iterate_records)                             |           |            |
| [iterate_zones](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.iterate_zones)                                 |           |            |
| [list_record_types](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.list_record_types)                         |           |            |
| [get_record](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.get_record)                                       |           |            |
| [get_zone](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.get_zone)                                           | #5        |            |
| [update_record](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.update_record)                                 |           |            |
| [update_zone](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.update_zone)                                     | #6        |            |
| [export_zone_to_bind_format](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.export_zone_to_bind_format)       |           |            |
| [export_zone_to_bind_zone_file](https://libcloud.readthedocs.io/en/stable/dns/api.html#libcloud.dns.base.DNSDriver.export_zone_to_bind_zone_file) |           |            |

## Zone

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| id       |           |
| domain   |           |
| type     |           |
| ttl      |           |
| driver   |           |
| extra    |           |

## Record

### Параметры

| Параметр | Поддержка |
| -------- | --------- |
| id       |           |
| name     |           |
| type     |           |
| data     |           |
| zone     |           |
| driver   |           |
| ttl      |           |
| extra    |           |

## Разработка

Для запуска тестов настроен tox. Для проверки коммитов настроен pre-commit.

Так же в проекте настроена автоматический запуск tox в GitHub Actions.

### Тесты

Тесты запускаются через tox, внутри используется [pytest](https://pytest.org/).

Для создания фикстур нужен установленный ключ окружения `DRIVER_TOKEN` с API ключём.

### Линтеры и форматтеры

Для запуска линтеров необходимо установить [pre-commit](https://pre-commit.com/). Линтеры запускаются командой `$ pre-commit run -a`.

#### Настройка `pre-commit`

Github Actions запускаются в `stage: commit`, поэтому в `.pre-commit-config.yaml` проверка `id: no-commit-to-branch` установлена в `stage: push`. Что бы проверка запускалась локально и не срабатывала в CI. Локально надо установить pre-commit хуки на пуши и на коммиты следующей командой:

```bash
$ pre-commit install --hook-type pre-commit --hook-type pre-push
```
