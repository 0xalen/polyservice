# BACKEND/PYTHON CODING PROJECT:

## GOALS
- Demonstrate proficiency in Django/Python
- Build something that scales gracefully & is easily extensible
- Write good API docs & Tests

## PROPMT
As a company expands internationally, there's a growing problem that many transportation suppliers cannot
give concrete zip codes, cities, etc that they serve. To combat this, we'd like to be able to define
custom polygons as their "service area" and we'd like for the owners of these shuttle companies to be
able to define and alter their polygons whenever they want, eliminating the need for company's employees
to do this boring grunt work.  We'd like to build a JSON REST API to help us solve this problem. 

The project should have API endpoints to create, update, delete, and retrieve information about providers. 
Batch operations are not necessary except for get. A provider should contain the following information:
- Name
- Email
- Phone Number
- Language
- Currency

Once a provider is created they should be able to start defining service areas. These service areas will 
be geojson polygons and should be stored in the database in a way that they can be retrieved and queried 
upon easily. There should be endpoints to create, update, delete, and get a polygon. Batch operations are 
not necessary except for get. A polygon should contain a name and price as well as the geojson information.

The project should have an API endpoint to query this data. It should take a lat/lng pair as arguments and 
return a list of all polygons that include the given lat/lng. The name of the polygon, provider's name, 
and price should be returned for each polygon. This operation should be FAST. The company has thousands of 
providers and hundreds of thousands of service areas.

All of this should be built in python/django with the corresponding API docs. 
The code should be well tested, clean (following standard  pep8 style) and has comments where appropriate.
