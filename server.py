from lyrica import lyrica
import os

# dynamicaly get the app environement PORT
port = int(os.environ.get('PORT', 5000))
# run the lyrica app
lyrica.run(host='0.0.0.0', port=port, debug=True)
