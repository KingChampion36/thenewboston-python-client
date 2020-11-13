from tnb.base_client import BaseClient


class Bank(BaseClient):
    def fetch_accounts(self):
        """
        Fetch accounts from a Bank
        Return response as Python object
        """
        return self.fetch('/accounts')

    def fetch_bank_transactions(self):
        """
        Get transactions from a Bank
        Return response as Python object
        """
        return self.fetch('/bank_transactions')

    def fetch_invalid_blocks(self):
        """
        Get invalid block from a Bank
        Return response as Python object
        """
        return self.fetch('/invalid_blocks')

    def fetch_validators(self):
        """
        Get validators from a Bank
        Return response as Python object
        """
        return self.fetch('/validators')

    def patch_account(self, account_number, node_id, trust, signature):
        """
        Send a PATCH request of an account to a Bank

        :param account_number: Specify the account will be patched
        :param node_id: The Node Identifier of the Bank
        :param trust: The value assigned to trust level of an account
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        resource = f'/accounts/{account_number}'
        body = {
            "message": {
                "trust": trust
            },
            "node_identifier": node_id,
            "signature": signature
        }

        return self.patch(resource, body=body)

    def connection_requests(self, node_id, signature):
        """
        Send a connection request to a Bank

        :param node_id: The Node Identifier of the Bank
        :param signature: The signature is signed by Bank's Node Identifier
            Signing Key

        Return response as Python object
        """
        body = {
            "message": {
                "ip_address": self.address,
                "port": self.port,
                "protocol": self.protocol
            },
            "node_identifier": node_id,
            "signature": signature,
        }

        return self.post('/connection_requests', body=body)

    def fetch_invalid_blocks(self):
        """
        Fetch invalid blocks from a Bank
        Return response as Python object
        """
        return self.fetch('/invalid_blocks')

    def post_invalid_block(self, block, block_identifier, primary_validator_node_identifier, node_identifier, signature):
        """
        Send a connection request to a Bank

        :param block: The invalid block
        :param block_identifier: ID for the block
        :param primary_validator_node_identifier: Primary Validator's Node Identifier
        :param node_identifier: Node Identifier of Confirmation Validator sending the request
        :param signature: Hex value of the signed message

        Return response as Python object
        """
        body = {
            "message": {
                "block": block,
                "block_identifier": block_identifier,
                "primary_validator_node_identifier": primary_validator_node_identifier
            },
            "node_identifier": node_identifier,
            "signature": signature
        }

        return self.post('/invalid_blocks', body=body)
