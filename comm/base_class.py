class BaseView(object):
	time_on_mars = 5

	def get_time_on_mars(self):
		"""
		Does what it takes to return a time on mars be it calculation
		or returning a property set on the object. Should return a property
		from the object if it is a constant. Should calcualte in the method
		if it is going to be dynanic
		"""
		return self.time_on_mars

	def get_context_data(self, **kwargs):
		context = super(BaseView, self).get_context_data(**kwargs)
		context['time_on_mars'] = self.get_time_on_mars()
		return context