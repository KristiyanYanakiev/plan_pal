from rest_framework import serializers
from proposals.models import Proposal
from votes.models import Vote


class ProposalSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Proposal
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Vote
        fields = '__all__'