from django.shortcuts import render
from .forms import InputForm
import math

def calculate_view(request):
    result_steps = []
    final_result = None
    error = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            # Check if values are numeric (already handled by form validation)
            result_steps.append(f"Received inputs: a = {a}, b = {b}, c = {c}")

            # Conditional checks
            if a < 1:
                result_steps.append("Warning: Value A is too small (less than 1).")
            if b == 0:
                result_steps.append("Note: Value B is zero and will not affect the result.")
            if c < 0:
                error = "Error: Value C cannot be negative."
            else:
                c_cubed = c ** 3
                result_steps.append(f"Computed c³ = {c_cubed}")

                sqrt_c_cubed = math.sqrt(c_cubed)
                result_steps.append(f"Square root of c³ = {sqrt_c_cubed}")

                if c_cubed > 1000:
                    operation_result = sqrt_c_cubed * 10
                    result_steps.append("Since c³ > 1000, multiplied sqrt(c³) by 10.")
                else:
                    operation_result = sqrt_c_cubed / a
                    result_steps.append("Since c³ ≤ 1000, divided sqrt(c³) by a.")

                final_result = operation_result + b
                result_steps.append(f"Added b to result: Final result = {final_result}")
        else:
            error = "Invalid input. Please enter numeric values."

    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {
        'form': form,
        'result_steps': result_steps,
        'final_result': final_result,
        'error': error
    })