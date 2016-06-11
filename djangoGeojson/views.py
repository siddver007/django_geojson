from django.http import HttpResponse, JsonResponse
from django.views.generic import View
import json
from djangoGeojson.models import *

##### Views for Providers 

# View to create a Provider/ User -- POST Http Request 
class createProviderView(View):

    def post(self, req):
        try:
            received_json_data = req.body
            processed_data = json.loads(received_json_data)
            if (set(['name', 'email', 'phone', 'lang', 'curr', 'pass']).issubset(processed_data) and
                len(processed_data.keys()) == 6):
                if not Provider.objects.filter(email = processed_data['email']):
                    provider = Provider()
                    provider.name = processed_data['name']
                    provider.email = processed_data['email']
                    provider.phone_number = processed_data['phone']
                    provider.language = processed_data['lang']
                    provider.currency = processed_data['curr']
                    provider.password = processed_data['pass']
                    provider.save()
                    return JsonResponse({'code':'201','success':'User successfully created'})
                else:
                    return JsonResponse({'code':'409','error':'User already exist'})    
            else:
                return JsonResponse({'code':'400', 'error':'Please check the request you made'})
        except ValueError:     
            return JsonResponse({'code':'400', 'error':'Please check the request you made'})

# View to retrieve Provider's/ User's Data -- GET Http Request
class getProviderView(View):

	def get(self,req):
		if 'email' in req.GET.keys() and 'pass' in req.GET.keys() and len(req.GET) == 2:
			provider = Provider.objects.filter(email = req.GET['email'], password = req.GET['pass'])
			if provider:
				return JsonResponse({'name': provider[0].name, 'email' : provider[0].email,
					'phone' : provider[0].phone_number, 'lang' : provider[0].language,
					'curr' : provider[0].currency})
			else:
				return JsonResponse({'code':'400','error':'User does not exist/ Invalid credentials'})	
		else:
			return JsonResponse({'code':'400','error':'Please check the request you made'})

# View to update Provider's/ User's Data -- PUT Http Request
class updateProviderView(View):

    def put(self,req):
        try:
            received_json_data = req.body
            processed_data = json.loads(received_json_data)
            if (set(['email', 'pass']).issubset(processed_data) and
                len(processed_data.keys()) > 2):
                provider = Provider.objects.filter(email = processed_data['email'], 
                password = processed_data['pass'])
                if provider:
                    if 'name' in processed_data.keys():
                        provider.update(name = processed_data['name'])
                    if 'phone' in processed_data.keys():    
                        provider.update(phone_number = processed_data['phone'])
                    if 'lang' in processed_data.keys():    
                        provider.update(language = processed_data['lang'])
                    if 'curr' in processed_data.keys():    
                        provider.update(currency = processed_data['curr'])
                    return JsonResponse({'code':'201','success':'User updated successfully'})
                else:
                    return JsonResponse({'code':'400','error':'User does not exist/ Invalid credentials'})    
            else:
                return JsonResponse({'code':'400', 'error':'Please check the request you made'})
        except ValueError:     
            return JsonResponse({'code':'400', 'error':'Please check the request you made'})	

# View to delete a Provider/ User alongwith their Regions/ Polygons -- DELETE Http Request
class deleteProviderView(View):

	def delete(self,req):
		if 'email' in req.GET.keys() and 'pass' in req.GET.keys() and len(req.GET) == 2:
			provider = Provider.objects.filter(email = req.GET['email'], password = req.GET['pass'])
			if provider:
				Region.objects.filter(email = provider[0].email).delete()
				provider.delete()
				return JsonResponse({'code':'200','success':'User successfully deleted'})
			else:
				return JsonResponse({'code':'400','error':'User does not exist/ Invalid credentials'})	
		else:
			return JsonResponse({'code':'400','error':'Please check the request you made'})	            		


##### Views for Regions/ Polygons

# View to create Regions/ Polygons for a Provider
## TBD : Unique GeoDatas for a Single/ Unique Provider 
class createPolygonView(View):
	
	def post(self,req):
		try:
			received_json_data = req.body
			processed_data = json.loads(received_json_data)
			if(set(['email', 'pass', 'price','geodata']).issubset(processed_data) and
				len(processed_data.keys()) == 4):
				provider = Provider.objects.filter(email = processed_data['email'],
				password = processed_data['pass'])
				if provider:
					region = Region()
					region.email = processed_data['email']
					region.price = processed_data['price']
					region.provider = provider[0].name
					region.geodata = json.dumps(processed_data['geodata'])
					region.save()
					return JsonResponse({'code':'201','success':'Region successfully added'})
				else:
					return JsonResponse({'code':'400','error':'User does not exist/ Invalid credentials'})	
			else:
				return JsonResponse({'code':'400', 'error':'Please check the request you made'})	
		except ValueError:
			return JsonResponse({'code':'400', 'error':'Please check the request you made'})

# Function to check whether a Coordinate is inside a Polygon --returns True if a coordinate is inside the polygon
def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside			

# View to retrieve Regions/ Polygons with their Providers based on the provided Latitude and Longitude
class getPolygonView(View):

	def get(self,req):
		try:
			if 'lat' in req.GET.keys() and 'lng' in req.GET.keys() and len(req.GET) == 2:
				regions = []
				for region in Region.objects.all():
					processed_data = json.loads(region.geodata)
					if (point_inside_polygon(float(req.GET['lat']),float(req.GET['lng']),
						processed_data['geometry']['coordinates'][0])):
						regions.append({'name' : processed_data['properties']['name'],
							'provider' : region.provider, 'price' : region.price, 
							'id': region.id})
				return HttpResponse(json.dumps(regions))	
			else:
				return JsonResponse({'code':'400','error':'Please check the request you made'})		
		except ValueError:
				return JsonResponse({'code':'400','error':'Please check the request you made'})

# View to update Regions/ Polygons for a the provided Unique ID 
class updatePolygonView(View):

    def put(self,req):
        try:
            received_json_data = req.body
            processed_data = json.loads(received_json_data)
            if (set(['email', 'pass', 'id']).issubset(processed_data) and
                len(processed_data.keys()) > 3):
                provider = Provider.objects.filter(email = processed_data['email'], 
                password = processed_data['pass'])
                if provider:
                	region = Region.objects.filter(email = provider[0].email, id = processed_data['id'])
                	if region:
	                    if 'price' in processed_data.keys():
	                        region.update(price = processed_data['price'])
	                    if 'geodata' in processed_data.keys():    
	                        region.update(geodata = json.dumps(processed_data['geodata']))
	                    return JsonResponse({'code':'201','success':'Region updated successfully'})
	                else:
	                	return JsonResponse({'code':'400','error':'Invalid ID'})    
                else:
                    return JsonResponse({'code':'400','error':'User does not exist/ Invalid credentials'})    
            else:
                return JsonResponse({'code':'400', 'error':'Please check the request you made'})
        except ValueError:     
            return JsonResponse({'code':'400', 'error':'Please check the request you made'})

# View to delete Regions/ Polygons for a the provided Unique ID
class deletePolygonView(View):

	def delete(self,req):
		if ('email' in req.GET.keys() and 'pass' in req.GET.keys() and 
			'id' in req.GET.keys() and len(req.GET) == 3):
			provider = Provider.objects.filter(email = req.GET['email'], password = req.GET['pass'])
			if provider:
				region = Region.objects.filter(email = provider[0].email, id = req.GET['id'])
				if region:
					region.delete()
				else:
					return JsonResponse({'code':'400','error':'Invalid ID'})	
				return JsonResponse({'code':'200','success':'Region successfully deleted'})
			else:
				return JsonResponse({'code':'400','error':'User does not exist/ Invalid credentials'})	
		else:
			return JsonResponse({'code':'400','error':'Please check the request you made'})            											
