#!/usr/bin/env tarantool

box.cfg{listen = 3301}
s = box.schema.space.create('tester',
    {if_not_exists = true})
s:format({
    {name = 'key', type = 'string'},
    {name = 'value', type = 'map'}
     })
s:create_index('primary', {
    if_not_exists = true,
    type = 'hash',
    parts = {'key'}
    })

box.schema.user.passwd('pass')
