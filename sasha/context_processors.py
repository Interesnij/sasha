from .forms import FeedbackForm

def form_feedback(request):
    return {'form_feedback': FeedbackForm}

def form_press(request):
    return {'form_press': PressForm}

def form_help(request):
    return {'form_help': HelpForm}
