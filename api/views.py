from rest_framework import generics, permissions
from proposals.models import Proposal
from .permissions import IsOwnerOrReadOnly
from .serializers import ProposalSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from proposals.models import Proposal
from votes.models import Vote


class ProposalListCreateAPI(generics.ListCreateAPIView):
    serializer_class = ProposalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Proposal.objects.filter(participants=user)

    def perform_create(self, serializer):
        proposal = serializer.save(owner=self.request.user)
        proposal.participants.add(self.request.user)


class ProposalDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProposalSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Proposal.objects.filter(participants=user)

class VoteAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        user = request.user

        try:
            proposal = Proposal.objects.get(pk=pk)
        except Proposal.DoesNotExist:
            return Response({'error': 'Proposal not found'}, status=status.HTTP_404_NOT_FOUND)

        if user == proposal.owner:
            return Response({'error': 'Owner cannot vote'}, status=status.HTTP_403_FORBIDDEN)

        if user not in proposal.participants.all():
            return Response({'error': 'Not allowed to vote'}, status=status.HTTP_403_FORBIDDEN)

        value = request.data.get('yes')

        if value not in [True, False]:
            return Response({'error': 'Invalid vote value'}, status=status.HTTP_400_BAD_REQUEST)

        vote, created = Vote.objects.update_or_create(
            user=user,
            proposal=proposal,
            defaults={'yes': value}
        )

        return Response({
            'message': 'Vote recorded',
            'yes': vote.yes
        }, status=status.HTTP_200_OK)