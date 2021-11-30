from django.shortcuts import render
from forms import FormAgendamento
from django.contrib import messages
from home.models import Agendamento


def agendamento(request):
    form = FormAgendamento(request.POST, request.FILES)
    if str(request.method) == "POST":
        if form.is_valid():
            data = form.cleaned_data.get("data")
            hora = form.cleaned_data.get("horario")
            medico = form.cleaned_data.get("medicos")

            if Agendamento.objects.order_by('-id').filter(data__icontains=data, horario__icontains=hora, medicos__nome__icontains=medico).exists():
                messages.add_message(request, messages.WARNING, 'Consulta já existe')
                return render(request, 'agendamento.html', {'form': form})

            messages.success(request, 'Consulta salva')
            form.save(commit=True)
            return render(request, 'agendamento.html', {'form': form})

        else:
            messages.error(request, 'Erro ao agendar')
            form = FormAgendamento()
            return render(request, 'agendamento.html', {'form': form})
    else:
        return render(request, 'agendamento.html', {'form': form})





