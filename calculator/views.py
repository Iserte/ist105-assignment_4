from django.shortcuts import render
from .forms import InputForm
import math

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            try:
                # Conditional checks
                if a < 1:
                    error = "Value A is too small. Please enter a number greater than or equal to 1."
                elif c < 0:
                    error = "Value C cannot be negative."
                else:
                    c_cubed = c ** 3
                    if c_cubed > 1000:
                        calc = math.sqrt(c_cubed) * 10
                    else:
                        calc = math.sqrt(c_cubed) / a
                    result = calc + b

                    # Optional message for b == 0
                    if b == 0:
                        result = f"{result} (Note: Value B did not affect the result.)"

            except Exception as e:
                error = f"An error occurred during calculation: {str(e)}"
        else:
            error = "Invalid input. Please enter numeric values."

    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {
        'form': form,
        'result': result,
        'error': error
    })