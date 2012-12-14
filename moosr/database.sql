drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    title string not null,
    short_title string not null,
    text string not null,
    username string not null
);
