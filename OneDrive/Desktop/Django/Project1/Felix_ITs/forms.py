from django import forms
from .models import Felix_class

class FelixForm(forms.ModelForm):
          class Meta:
                  model =Felix_class
                  fields =['name','img','type','duration']

          def __init__(self, *args, **kwargs):
                  super(FelixForm,self).__init__(*args,**kwargs)
                  self.fields['name'].widget.attrs.update({
                          'class':'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500'
                  })

                  self.fields['img'].widget.attrs.update({
                          'class':'w-full px-4 py-2 border border-gray-300 rounded bg-white'
                  })

                  self.fields['type'].widget.attrs.update({
                          'class':'w-full px-4 py-2 border border-gray-300 rounded'
                  })

                  self.fields['duration'].widget.attrs.update({
                          'class':'w-full px-4 py-2 border border-gray-300 rounded'
                  })
                  
        