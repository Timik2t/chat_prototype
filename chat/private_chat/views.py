from django.views.generic import ListView
from private_chat.models import Dialog, Message
from private_chat.forms import MessageForm


class ChatView(ListView):
    template_name = 'chat.html'
    model = Dialog


class MessagesListView(ListView):
    template_name = 'messages.html'
    model = Message

    def get_queryset(self):
        dialog_id = self.kwargs['pk']
        return Message.objects.filter(
            dialog_id=dialog_id
            ).order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dialog = Dialog.objects.get(pk=self.kwargs['pk'])
        context['dialog'] = dialog
        context['form'] = MessageForm(initial={'dialog': dialog})
        return context
