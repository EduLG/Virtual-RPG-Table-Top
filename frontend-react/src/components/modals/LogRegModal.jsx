import React from "react";
import {
  Dialog,
  Button,
  Text,
  Heading,
  TextField,
  Flex,
} from "@radix-ui/themes";

const LoginModal = ({
  visible,
  setVisible,
  mode,
  userName,
  setUserName,
  password,
  setPassword,
  email,
  setEmail,
}) => {
  return (
    <Dialog.Root open={visible} onOpenChange={setVisible}>
      <Dialog.Content maxWidth="400px">
        {mode === "login" ? (
          <Flex direction="column" gap="3">
            <Heading size="7">Log in</Heading>

            <Text>User Name</Text>
            <TextField.Root
              value={userName}
              placeholder="Username"
              onChange={(e) => setUserName(e.target.value)}
            />

            <Text>Password</Text>
            <TextField.Root
              value={password}
              type="password"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
            />
            <br />
            <Button>Login</Button>
          </Flex>
        ) : (
          <Flex direction="column" gap="3">
            <Heading size="7">Register</Heading>

            <Text>Email</Text>
            <TextField.Root
              value={email}
              placeholder="Email"
              onChange={(e) => setEmail(e.target.value)}
            />

            <Text>User Name</Text>
            <TextField.Root
              value={userName}
              placeholder="Username"
              onChange={(e) => setUserName(e.target.value)}
            />

            <Text>Password</Text>
            <TextField.Root
              value={password}
              type="password"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
            />
            <br />
            <Button>Register</Button>
          </Flex>
        )}
      </Dialog.Content>
    </Dialog.Root>
  );
};

export default LoginModal;
