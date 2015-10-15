/*Ex 1*/
select * from Tenants inner join ApartmentTenants as AT on Tenants.id = AT.tenant_id
having count(tenant_id) > 1;

/*Ex 2*/

select B.id as building_id, count(B.id) as open_requests from Requests
inner join Apartments as A on
    Requests.apartment_id = A.id
inner join Buildings as B on
    A.building_id = B.id
where Requests.status = "Open" group by B.id;

/*Ex 3*/

Update Requests as R
inner join Apartments as A on
	R.apartment_id = A.id
inner join Buildings as B on
	A.building_id = B.id
set R.status = 'Closed'
where B.id = 1;


/*Ex 4*/
1 - Inner Join, used to join two tables and combine rows from both, if for a given combination either table is empty (doesnt have the row), the result is omitted
2 - Left Join, used to join two tables and prioritize rows from the first table
3 - Right Join, used to join two tables and prioritize rows from the second table
....few others....

/*Ex 5*/
