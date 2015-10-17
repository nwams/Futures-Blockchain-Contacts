drop table if exists entries;
create table entries (
  buyerid text not null,
  transaction text not null,
  deliverydatetransaction text not null
  canceltransaction text not null
);