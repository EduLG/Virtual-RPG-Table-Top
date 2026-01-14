import React from "react";
import {
  Dialog,
  Button,
  Text,
  Heading,
  TextField,
  Flex,
} from "@radix-ui/themes";

const LoginModal = ({ visible, setVisible, mode }) => {
  return (
    <Dialog.Root open={visible} onOpenChange={setVisible}>
      <Dialog.Content maxWidth="400px">
        {mode === "login" ? (
          <Flex direction="column" gap="3">
            <Heading size="4">Log in</Heading>

            <Text>User Name</Text>
            <TextField.Root placeholder="Username" />

            <Text>Password</Text>
            <TextField.Root type="password" placeholder="Password" />

            <Button>Login</Button>
          </Flex>
        ) : (
          <Flex direction="column" gap="3">
            <Heading size="4">Register</Heading>

            <Text>Email</Text>
            <TextField.Root placeholder="Email" />

            <Text>User Name</Text>
            <TextField.Root placeholder="Username" />

            <Text>Password</Text>
            <TextField.Root type="password" placeholder="Password" />

            <Button>Register</Button>
          </Flex>
        )}
      </Dialog.Content>
    </Dialog.Root>
  );
};

export default LoginModal;
